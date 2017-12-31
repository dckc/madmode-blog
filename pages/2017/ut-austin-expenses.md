title: College Expense Tracking in BASIC09
date: 2017-12-30
published: True
tags: ['coco', 'finances', 'economics', 'America', 'ipynb']

It's no wonder my kids struggle so much more to pay for college:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Hours of minimum wage work needed to pay for four years of public college<br><br>Boomer: 306<br>Millennial: 4,449<br><br>Source: <a href="https://t.co/3ZZDpC9Fgw">https://t.co/3ZZDpC9Fgw</a></p>&mdash; Ryan Carson (@ryancarson) <a href="https://twitter.com/ryancarson/status/943468921834717185?ref_src=twsrc%5Etfw">December 20, 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

In my freshman year at U.T.  Austin, I wrote a [BASIC09][] program
to track my expenses:

```basic
PRINT CHR$(12); "Expenses -- by Dan Connolly"
PRINT "<A> - Edit Accounts"
PRINT "<E> - Journal Entry"
PRINT "<R> - Generate Report"
PRINT "<C> - Clean up file"
PRINT "<Q> - Quit"
RUN Choose("Choice: ","AERCQ",Choice)
```

[BASIC09]: https://en.wikipedia.org/wiki/BASIC09

I found a `Rpt02.22` report that shows tuition of about $500, mostly covered by a scholarship:


```python
def _cocodisks():
    from pathlib import Path
    return Path('1986-cocodisks')

EXP = _cocodisks() / 'archive' / 'PRG-x' / 'EXP'
tx_lines = list((EXP / 'Rpt02.22').open())
tx_lines = tx_lines[1:]  # skip blank line
tx_lines[:2] + tx_lines[8:11]
```




    [u'Date        Description   Amount  Source Name   Src Bal Dest Name     Dest Bal\n',
     u'----------- ------------- ------- ------------- ------- ------------- --------\n',
     u' 9-01-86:11 Books          117.85 Cash           182.15 Books/Supplie  117.85\n',
     u' 9-15-86:11 Scholarship    296.46 National Meri -296.46 U T            496.28\n',
     u' 9-15-86:15 Scholarship     78.54 National Meri -375.00 Cash           260.69\n']



The last page of the report shows account balances:


```python
acct_hd_ix = next(ix for ix, line in enumerate(tx_lines) if line.strip().startswith('Num'))
acct_lines = tx_lines[acct_hd_ix:]
acct_lines[:5]
```




    [u' Num  Account Name  Balance\n',
     u'----  ------------- -------\n',
     u'   1: Cash             63.51\n',
     u'   2: Checks           28.00\n',
     u'   3: Bank Account    888.52\n']



But the `Jrnl` data file goes thru March 12...

```
1986-cocodisks/archive/PRG-x/EXP$ ls -l Jrnl 
-r--r--r-- 1 connolly connolly 5443 Mar 12  1987 Jrnl
986-cocodisks/archive/PRG-x/EXP$ sha1sum Jrnl 
3f75dbc8bcdac51874259c44ef1fcad55fe068e0  Jrnl
```

... where that report only goes thru Feb 22:


```python
tx_lines[acct_hd_ix - 7: acct_hd_ix - 5]
```




    [u' 2-22-87:11 Bus               .50 Cash            63.51 Living Expens  138.94\n',
     u' 2-22-87:15 NOW -----         .00                   .00                   .00\n']



## Porting BASIC09 File Reading Code to Python

I spent some time poring over the [EXP][] source code (`08c15cc`)
to get the data out:

```
1986-cocodisks/archive/PRG-x/EXP$ wc *.b
    0    38   300 Acct.b
    3   506  4490 Entry.b
    7   564  5141 Exp.b
    1   125  1021 Rec.b
    2   142  1269 Report.b
   13  1375 12221 total
```

[EXP]: https://bitbucket.org/DanC/madmode-blog/src/08c15cccd1ef?at=default
[or]: https://bitbucket.org/DanC/madmode-blog/src/82e8cc458606f46df7c2d7ef3393eb09448eec91/static/1986-cocodisks/archive/PRG-x/EXP/?at=default

The `file` command even recognizes the compiled format:

```
1986-cocodisks/archive/PRG-x/EXP$ file Expenses 
Expenses: OS9/6809 module: BASIC I-code subroutine
```



```python
import pandas as pd
import numpy as np
dict(pandas=pd.__version__, numpy=np.__version__)
```




    {'numpy': '1.10.1', 'pandas': u'0.17.1'}



The file is just 5K. These days it's trivial to read that into memory,
but my coco only had 16K of RAM, upgraded from 4K.


```python
Jrnl = (EXP / 'Jrnl').open('rb').read()
len(Jrnl)
```




    5443



The transaction format is mostly straightforward,
though I'm glad I had the source code to decode the `key` field:


```python
import datetime
from collections import namedtuple, OrderedDict
import struct

class Trans(namedtuple('Trans', 'key, desc, amt, db, cr')):
    """
    TYPE Trans=Key:INTEGER; Desc:STRING[13]; Amt:REAL; DB,CR:BYTE
    """
    struct = struct.Struct('>h13s5sBB')

    @classmethod
    def unpack(cls, data):
        it = cls(*cls.struct.unpack(data[:cls.struct.size]))
        it = it._replace(desc=Basic09.string(it.desc),
                         amt=Basic09.real(it.amt))
        return it

    @property
    def indx(self):
        return self.key % 32 + 1

    @property
    def date(self):
        r"""
        port of PROCEDURE DateStr

        Indx=MOD(Key,32)+1 \Copy=Key/32
        Day=MOD(Copy,31)+1 \Copy=Copy/31
        Month=MOD(Copy,12)+1 \Copy=Copy/12
        Year=86+Copy
        """
        copy = self.key / 32
        day = copy % 31 + 1
        copy = copy / 31
        month = copy % 12 + 1
        copy = copy / 12
        year = 1986 + copy
        try:
            return datetime.date(year, month, day)
        except ValueError:  # Nov 31???
            return datetime.date(year, month, day - 1)

    def as_dict(self):
        return dict(date=self.date, indx=self.indx,
                    desc=self.desc, amt=round(self.amt, 2), db=self.db, cr=self.cr)
```

I couldn't figure out how to decode the floating point
account balances until I realized I was comparing them
against the Feb 22 report rather than their March 12 values.

> Type REAL

> REAL numbers are stored in 5 consecutive memory bytes.
> The first byte is the (8-bit) exponent in binary two's-complement representation.
> The next four bytes are the binary sign-and-magnitude representation of the mantissa;
> the mantissa in the first 31 bits, and the sign of the mantissa in the last
> (least significant) bit of the last byte of the real quantity.
>  -- [BASIC09: Programming Language Reference Manual][ref]
>  Copyright (c) 1983 Microware Systems Corporation

[ref]: http://www.roug.org/soren/6809/basic09.pdf


```python
class Basic09(object):
    @classmethod
    def string(cls, data):
        return data[:data.find('\xff')] if '\xff' in data else data

    @classmethod
    def real(cls, b5):
        exp, mag = struct.unpack('>bI', b5)
        sgn = -1 if (mag % 2) else 1
        mag = mag >> 1
        mag = mag * 1.0 / (2 ** 31)
        return mag * (2 ** exp) * sgn
```

The overall file format is a linked list:


```python
class Global(namedtuple('Global', 'trx, head, tail, rec, avail, name, bal, file')):
    """
    TYPE Global=Trx:Trans; Head,Tail,Rec,Avail:INTEGER; Name(32):STRING
    """
    struct = struct.Struct('>hhhh%ds%dsB' % (32 * 13, 32 * 5))
    @classmethod
    def unpack(cls, data):
        trx = Trans.unpack(data)
        data = data[Trans.struct.size:]
        it = cls(*((trx,) + cls.struct.unpack(data[:cls.struct.size])))
        ea = 13
        name = [Basic09.string(it.name[ea * ix:ea * (ix + 1)]) for ix in range(32)]
        ea = 5
        bal = [Basic09.real(it.bal[ea * ix:ea * (ix + 1)]) for ix in range(32)]
        return it._replace(name=name, bal=bal)

    def accounts(self):
        a = pd.DataFrame(dict(name=self.name, bal=self.bal), columns=['name', 'bal'])
        a.index = a.index + 1
        return a

    def iter_trans(self, jrnl):
        here = self.rec
        while True:
            after, before = struct.unpack('>HH', jrnl[here + Trans.struct.size:][:4])
            here = after
            if here == 0:
                break
            yield Trans.unpack(jrnl[here:])

G = Global.unpack(Jrnl)
print G.trx
print dict(head=G.head, tail=G.tail, rec=G.rec, avail=G.avail)
ut_accounts = G.accounts()
ut_accounts.head(3)
```

    Trans(key=32767, desc='Delphi Bill', amt=46.80000001192093, db=10, cr=19)
    {'avail': 5443, 'rec': 0, 'tail': 5313, 'head': 607}





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>bal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cash</td>
      <td>76.220001</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Checks</td>
      <td>552.950000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bank Account</td>
      <td>890.420005</td>
    </tr>
  </tbody>
</table>
</div>




```python
journal = pd.DataFrame.from_records(
    (tx.as_dict() for tx in G.iter_trans(Jrnl)),
    columns=['date', 'indx', 'desc', 'amt', 'db', 'cr']).set_index(['date', 'indx'])

journal = journal.merge(ut_accounts[['name']], left_on='db', right_index=True)
journal = journal.rename(columns=dict(name='Source Name'))
journal = journal.merge(ut_accounts[['name']], left_on='cr', right_index=True)
journal = journal.rename(columns=dict(name='Dest Name'))
journal = journal.sort_index()

journal.iloc[6:9]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>desc</th>
      <th>amt</th>
      <th>db</th>
      <th>cr</th>
      <th>Source Name</th>
      <th>Dest Name</th>
    </tr>
    <tr>
      <th>date</th>
      <th>indx</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-09-01</th>
      <th>11</th>
      <td>Books</td>
      <td>117.85</td>
      <td>1</td>
      <td>23</td>
      <td>Cash</td>
      <td>Books/Supplie</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1986-09-15</th>
      <th>11</th>
      <td>Scholarship</td>
      <td>296.46</td>
      <td>7</td>
      <td>20</td>
      <td>National Meri</td>
      <td>U T</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Scholarship</td>
      <td>78.54</td>
      <td>7</td>
      <td>1</td>
      <td>National Meri</td>
      <td>Cash</td>
    </tr>
  </tbody>
</table>
</div>



Computing running balances with pandas with `cumsum` was fun.


```python
def running_balance(journal):
    cr = journal[['cr', 'amt']].rename(columns=dict(cr='acct'))
    cr['col'] = 'cr'
    db = journal[['db', 'amt']].rename(columns=dict(db='acct'))
    db['col'] = 'db'
    db.amt = -db.amt
    ea = cr.append(db).sort_index()
    ea['bal'] = ea.groupby('acct').amt.cumsum()
    cum = ea.reset_index().pivot_table(index=['date', 'indx'], columns='col', values=['bal'])
    journal = journal.copy()
    journal.insert(len(journal.columns) - 1, 'Src Bal', cum.bal.db)
    journal['Dest Bal'] = cum.bal.cr
    return journal

running_balance(journal).to_csv('ut-austin-journal.csv')

running_balance(journal).iloc[6:9]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>desc</th>
      <th>amt</th>
      <th>db</th>
      <th>cr</th>
      <th>Source Name</th>
      <th>Src Bal</th>
      <th>Dest Name</th>
      <th>Dest Bal</th>
    </tr>
    <tr>
      <th>date</th>
      <th>indx</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1986-09-01</th>
      <th>11</th>
      <td>Books</td>
      <td>117.85</td>
      <td>1</td>
      <td>23</td>
      <td>Cash</td>
      <td>182.15</td>
      <td>Books/Supplie</td>
      <td>117.85</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1986-09-15</th>
      <th>11</th>
      <td>Scholarship</td>
      <td>296.46</td>
      <td>7</td>
      <td>20</td>
      <td>National Meri</td>
      <td>-296.46</td>
      <td>U T</td>
      <td>496.28</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Scholarship</td>
      <td>78.54</td>
      <td>7</td>
      <td>1</td>
      <td>National Meri</td>
      <td>-375.00</td>
      <td>Cash</td>
      <td>260.69</td>
    </tr>
  </tbody>
</table>
</div>



And with that, we have recovered the journal data from the report:


```python
tx_lines[:2] + tx_lines[8:11]
```




    [u'Date        Description   Amount  Source Name   Src Bal Dest Name     Dest Bal\n',
     u'----------- ------------- ------- ------------- ------- ------------- --------\n',
     u' 9-01-86:11 Books          117.85 Cash           182.15 Books/Supplie  117.85\n',
     u' 9-15-86:11 Scholarship    296.46 National Meri -296.46 U T            496.28\n',
     u' 9-15-86:15 Scholarship     78.54 National Meri -375.00 Cash           260.69\n']



And we can compute account balances:


```python
src_bal = journal.groupby('db')[['amt']].sum()
dst_bal = journal.groupby('cr')[['amt']].sum()
bal = src_bal.merge(dst_bal, left_index=True, right_index=True, how='outer', suffixes=['_src', '_dst']).fillna(0)
bal['balance'] = bal.amt_dst - bal.amt_src
bal = bal.drop(['amt_src', 'amt_dst'], axis=1)
bal = bal.merge(ut_accounts[['name']], left_index=True, right_index=True)[['name', 'balance']]
bal.to_csv('ut-austin-accounts.csv', index_label='acct_num')
bal[:3]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>balance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Cash</td>
      <td>76.22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Checks</td>
      <td>552.95</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bank Account</td>
      <td>890.42</td>
    </tr>
  </tbody>
</table>
</div>


