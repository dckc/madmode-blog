# grok-stmt

I track my finances with GnuCash; I used to read quarterly retirement
account statements pretty regularly, but lately I find myself as much
as 18 months (6 statements) behind, so that extracting the details out
of each statement looks rather tedious.

I've had some luck with using inotify to watch my downloads folder and
automatically process Simple transactions from JSON format to QFX.
I'd like to do likewise with these statements.

I've done PDF scraping with a combination of some debian package like
pdf2text and a python script, but I aim to move more of my world to
SES where ocap discipline can be enforced by machine.
