if [ "$1" == "-h" ] || [ "$2" == "-h" ] || [ "$#" -eq 0 ]
	then
	echo "Usage: ./test.sh [-h] [-v] -a|-NUM"
	echo "	-h   : display this help message"
	echo "	-v   : runs expert_sys.py with verbose option"
	echo "	-a   : runs every tests"
	echo "	-NUM : runs test number NUM"
	exit
fi


if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-1" ] || [ "$2" == "-1" ]
	then
	printf "A + B => C\nA => B\n=A\n?C" > testfile.out
	echo "\033[0;1mTest 1:   ------------------------\033[0;0m"
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-2" ] || [ "$2" == "-2" ]
	then
	echo "\033[0;1mTest 2:   ------------------------\033[0;0m"
	printf "A + B => C\n!A => B\n=AC\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-3" ] || [ "$2" == "-3" ]
	then
	echo "\033[0;1mTest 3:   ------------------------\033[0;0m"
	printf "A | B => C\n=A\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-4" ] || [ "$2" == "-4" ]
	then
	echo "\033[0;1mTest 4:   ------------------------\033[0;0m"
	printf "A + ( B | D ) => C\n!A => B\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-5" ] || [ "$2" == "-5" ]
	then
	echo "\033[0;1mTest 5:   ------------------------\033[0;0m"
	printf "A ^ B => C\n!A => B\n=A\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-6" ] || [ "$2" == "-6" ]
	then
	echo "\033[0;1mTest 6:   ------------------------\033[0;0m"
	printf "A + ( B + ( D + E ) ) => C\nA => B\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-7" ] || [ "$2" == "-7" ]
	then
	echo "\033[0;1mTest 7:   ------------------------\033[0;0m"
	printf "!A ^ ( B | D ) => C\nA => B\n=A\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-8" ] || [ "$2" == "-8" ]
	then
	echo "\033[0;1mTest 8:   ------------------------\033[0;0m"
	printf "!A ^ ( !B ^ D ) => C\nA => B\n=\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-9" ] || [ "$2" == "-9" ]
	then
	echo "\033[0;1mTest 9:   ------------------------\033[0;0m"
	printf "!A ^ ( !B ^ ( D ^ !D ) ) => C\nA => B\n=A\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-10" ] || [ "$2" == "-10" ]
	then
	echo "\033[0;1mTest 10:   -----------------------\033[0;0m"
	printf "!A ^ ( !B ^ D ) => C\nA => B\n=ABD\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-11" ] || [ "$2" == "-11" ]
	then
	echo "\033[0;1mTest 11:   -----------------------\033[0;0m"
	printf "!A ^ ( !B ^ ( D + A ) ) => C\nA => B\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-12" ] || [ "$2" == "-12" ]
	then
	echo "\033[0;1mTest 12:   -----------------------\033[0;0m"
	printf "A + ( B + ( D + ( E + F ) ) ) => C\nA => B\nB => D\nD => E\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-13" ] || [ "$2" == "-13" ]
	then
	echo "\033[0;1mTest 13:   -----------------------\033[0;0m"
	printf "A + ( B + ( D + ( E + F ) ) ) => C\nA => B\nB => D\nD => E\nD => F\n=A\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-14" ] || [ "$2" == "-14" ]
	then
	echo "\033[0;1mTest 14:   -----------------------\033[0;0m"
	printf "A ^ !A => C\n=A\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-15" ] || [ "$2" == "-15" ]
	then
	echo "\033[0;1mTest 15:   -----------------------\033[0;0m"
	printf "A ^ B => C\nA => B\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-16" ] || [ "$2" == "-16" ]
	then
	echo "\033[0;1mTest 16:   -----------------------\033[0;0m"
	printf "A ^ B => C\nA => !B\n=AB\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-17" ] || [ "$2" == "-17" ]
	then
	echo "\033[0;1mTest 17:   -----------------------\033[0;0m"
	printf "( A + B ) + D => C\nA => B\n=AD\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-18" ] || [ "$2" == "-18" ]
	then
	echo "\033[0;1mTest 18:   -----------------------\033[0;0m"
	printf "( ( ( ( A ^ B ) + D ) | E ) ^ F ) => C\nB => !A + D\nA => B\n( A ^ ( !F + !E ) ) => F + E\nF + ( E + !A ) => !F\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-19" ] || [ "$2" == "-19" ]
	then
	echo "\033[0;1mTest 19:   -----------------------\033[0;0m"
	printf "( ( ( ( A ^ B ) + D ) | E ) ^ F ) => C\nB => !A + D\nA => B\n( A ^ ( !F + !E ) ) => F + E\nF + ( E + !A ) => !F\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-20" ] || [ "$2" == "-20" ]
	then 
	echo "\033[0;1mTest 20:   -----------------------\033[0;0m"
	printf "( ( (A ^ B ) + D ) | E ) ^ F => C\nB => !A + D\nA => B\n( A ^ ( !F + !E ) ) => F + E\nF + ( E + !A ) => !F\n=\n?ABCDEF" > testfile.out
	echo "\033[31mA,B,C,D sould be false\033[0m"
	echo "\033[32mE,F should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-21" ] || [ "$2" == "-21" ]
	then
	echo "\033[0;1mTest 21:   -----------------------\033[0;0m"
	printf ") A + B ( => C\n=A\n?C" > testfile.out
	echo "\033[33mParentheses error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-22" ] || [ "$2" == "-22" ]
	then
	echo "\033[0;1mTest 22:   -----------------------\033[0;0m"
	printf "( ( ( A ^ B ) + D ) | E ) ^ F ) => C\nB => !A + D\nA => B\n( A ^ ( !F + !E ) ) => F + E\nF + ( E + !A ) => !F\n=A\n?ABCDEF" > testfile.out
	echo "\033[33mParentheses error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-23" ] || [ "$2" == "-23" ]
	then
	echo "\033[0;1mTest 23:   -----------------------\033[0;0m"
	printf "( ( ( ( A^B )+D )|E )^F )=>C\nB=>!A+D\nA=>B\n(A^(!F+!E))=>F+E\nF+(E+!A)=>!F\n=A\n?C" > testfile.out
	echo "\033[31mC should be false\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-24" ] || [ "$2" == "-24" ]
	then
	echo "\033[0;1mTest 24:   -----------------------\033[0;0m"
	printf "( A B ) => C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-25" ] || [ "$2" == "-25" ]
	then
	echo "\033[0;1mTest 25:   -----------------------\033[0;0m"
	printf "( A + + B) => C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-26" ] || [ "$2" == "-26" ]
	then
	echo "\033[0;1mTest 26:   -----------------------\033[0;0m"
	printf "( ) A + B => C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-27" ] || [ "$2" == "-27" ]
	then
	echo "\033[0;1mTest 27:   -----------------------\033[0;0m"
	printf "(A+B)+(B+A)=> C\n=AB\n?C" > testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-28" ] || [ "$2" == "-28" ]
	then
	echo "\033[0;1mTest 28:   -----------------------\033[0;0m"
	printf "(A + !1)=> C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-29" ] || [ "$2" == "-29" ]
	then
	echo "\033[0;1mTest 29:   -----------------------\033[0;0m"
	printf "(A B)=> C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-30" ] || [ "$2" == "-30" ]
	then
	echo "\033[0;1mTest 30:   -----------------------\033[0;0m"
	printf "(A + B) C => C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-31" ] || [ "$2" == "-31" ]
	then
	echo "\033[0;1mTest 31:   -----------------------\033[0;0m"
	printf "=> C\n=A\n?C" > testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-32" ] || [ "$2" == "-32" ]
	then
	echo "\033[0;1mTest 32:   -----------------------\033[0;0m"
	printf ""> testfile.out
	echo "\033[33mNothing\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-33" ] || [ "$2" == "-33" ]
	then
	echo "\033[0;1mTest 33:   -----------------------\033[0;0m"
	printf "= ? "> testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-34" ] || [ "$2" == "-34" ]
	then
	echo "\033[0;1mTest 34:   -----------------------\033[0;0m"
	printf "zaz"> testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-35" ] || [ "$2" == "-35" ]
	then
	echo "\033[0;1mTest 35:   -----------------------\033[0;0m"
	printf "A => \n=B\n?C"> testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-36" ] || [ "$2" == "-36" ]
	then
	echo "\033[0;1mTest 36:   -----------------------\033[0;0m"
	printf "A => yolo\n=B\n?C"> testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-37" ] || [ "$2" == "-37" ]
	then
	echo "\033[0;1mTest 37:   -----------------------\033[0;0m"
	printf "yolo => C\n=B\n?C"> testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-38" ] || [ "$2" == "-38" ]
	then
	echo "\033[0;1mTest 38:  -----------------------\033[0;0m"
	printf "A + B => C\n=A\n=B\n=AB\n?C"> testfile.out
	echo "\033[31mC should be false\033[0m"
	echo "\033[31mC should be false\033[0m"
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-39" ] || [ "$2" == "-39" ]
	then
	echo "\033[0;1mTest 39:  -----------------------\033[0;0m"
	printf "A + B => C\n A => B\n=A\n=B\n=AB\n?C"> testfile.out
	echo "\033[32mC should be true\033[0m"
	echo "\033[31mC should be false\033[0m"
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-40" ] || [ "$2" == "-40" ]
	then
	echo "\033[0;1mTest 40:   -----------------------\033[0;0m"
	printf "A + B => C\n C => !C\n=A\n=B\n?ABC"> testfile.out
	echo "\033[31mC should be false\033[0m\n"
	echo "\033[31mAC should be false\033[0m\n\033[32mB should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-41" ] || [ "$2" == "-41" ]
	then
	echo "\033[0;1mTest 41:   -----------------------\033[0;0m"
	printf "A + B => C\n=AB\n?C"> testfile.out
	echo "\033[32mC should be true\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
if [ "$1" == "-a" ] || [ "$2" == "-a" ] || [ "$1" == "-42" ] || [ "$2" == "-42" ]
	then
	echo "\033[0;1mTest 42:   -----------------------\033[0;0m"
	printf "21 + 21 => 42\n=42\n?Vie, Univers et le reste"> testfile.out
	echo "\033[33mSyntax error\033[0m"
	if [ "$1" == "-v" ] || [ "$2" == "-v" ]
		then
			./expert_sys.py -v testfile.out
		else
			./expert_sys.py testfile.out
		fi
	printf "\n"
fi
echo "\033[0m"
