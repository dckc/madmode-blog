PROCEDURE ReportTYPE Trans=Key:INTEGER; Desc:STRING[13]; Amt:REAL; DB,CR:BYTETYPE Global=Trx:Trans; Head,Tail,Rec,Avail:INTEGER; Name(32):STRING
[13]; Bal(32):REAL; File:BYTEPARAM G:GlobalDIM Out,Line:BYTEDIM OutPath:STRINGDIM Move,A:INTEGERDIM First,Last:INTEGERDIM Sbal(32):REALINPUT "Start Date: ",a$RUN datenum(a$,First)INPUT "End Date: ",a$RUN datenum(a$,Last)INPUT "Output Pathname: ",OutPathON ERROR GOTO 100CREATE #Out,OutPath:WRITERUN Point(TRUE,G.File,1,0,G.Rec)SEEK #G.File,G.RecGET #G.File,G.TrxFOR A=1 TO 32G.Bal(A)=0NEXT ARUN PosFil(G,0,First)Sbal=G.BalMove=1 \Line=1REPEAT RUN JLine(Out,Line,G.Name,G.Bal,G.Trx)Line=Line+1RUN PosFil(G,Move,Last)UNTIL Move=0Line=1FOR A=1 TO 32IF G.Bal(A)<>Sbal(A) THEN RUN SLine(Out,Line,G.Name(A),G.Bal(A),Sbal(A),A)Line=Line+1ENDIF NEXT ACLOSE #OutEND 100 PRINT "Error: "; ERRINPUT a$END PROCEDURE SLinePARAM Path,Line:BYTEPARAM Name:STRING[13]PARAM Bal,IBal:REALPARAM Num:INTEGERDIM Min,Max:BYTEMin=4 \Max=60IF Line<Min OR Line>Max THEN PRINT #Path,CHR$(12)PRINT #Path," Num  Account Name   Start    Net     End"PRINT #Path,"----  ------------- ------- ------- -------"Line=4ENDIF PRINT #Path USING "I4>,': ',S13,3(R8.2>)",Num,Name,IBal,Bal-IBal
,Bal