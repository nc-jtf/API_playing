text = '''MESSAGE
	Message sender Ran..35
	Message recipient Ran..35
	Preparation date and time Ran19 G0002
	Message identification Ran..35 G0137
T1120
	Message type Ran6CL060
	Correlation identifier Dan..35 B1833
C0511
G0137
R0008
T1120
---TRANSIT OPERATION
	MRN Ran18 G0002
R0028
	Declaration type Ran..5CL231B1922
R0601
R0909
R0911
	TIR Carnet number Dan..12 B1913
C0411
R0990
	Declaration acceptance date Ran10 G0002
	Release date Ran10 G0002
	Security Rn1CL217
	Reduced dataset indicator Rn1CL027
	Specific circumstance indicator Dan3CL296C0812
	Binding itinerary Rn1CL027
---CUSTOMS OFFICE OF DEPARTURE
	Reference number Ran8CL171R0901
---CUSTOMS OFFICE OF DESTINATION (DECLARED)
	Reference number Ran8CL172R0901
R0904
R0905
---CUSTOMS OFFICE OF TRANSIT (DECLARED)
	Sequence number Rn..5 R0987
	Reference number Ran8CL173B1813
G0142
R0003
R0006
R0906
	Arrival date and time (estimated) Dan19 B1831
B1903
C0598
G0002
R0004
---CUSTOMS OFFICE OF EXIT FOR TRANSIT (DECLARED)
	Sequence number Rn..5 R0987
	Reference number Ran8CL175R0103
---HOLDER OF THE TRANSIT PROCEDURE
	Identification number Oan..17 G0120
	TIR holder identification number Dan..17 C0904
G0002
	Name Ran..70 E1104
------ADDRESS
	Street and number Ran..70 E1104
	Postcode Dan..17 C0505
E1102
	City Ran..35
	Country Ra2CL199
---CONTROL RESULT
	Code Ran2CL196G0126
R0910
R0912
Page 6 of
376DDNTA for NCTS P5. Release 5.15.1 Aligned to DDNTA RFC-List.37
REF:DDNTA_APP_Q2
Appendix Q2: Technical Message Structure
2. Message Structure for: IE001
CSE 51.8.2'''

import re
pattern = r".*?\sCL\d{3}"
# pattern = r'(\S+\s)?\S+ CL \d{3}'
matches = re.findall(pattern, text)

print (matches)