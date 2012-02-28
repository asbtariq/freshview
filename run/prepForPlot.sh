# This script removes lines with an @ and the last line 'END' from the fort.16 output file


#stem = {basename $1} .inp
inpF = 28si28.0
echo inpF
runID = w21
echo stem = $inpF$runID
cd run
fresco < ../inp/$inpF.inp
cd ..
grep -v '@' run/fort.16 | grep -v 'END' > out/$stem.out

