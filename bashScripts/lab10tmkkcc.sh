
#!/bin/bash
#created by Timothy Kerr [TMKKCC]

#6 number menu assignment


date=$(date)
user=$USER
green='\e[32m'
blue='\e[34m'
cleard='\e[0m'

echo -e "Hello "$user""
sleep 1

echo "It is currently "$date""
sleep 1

while true
do
	echo "[====================]"
	echo -e $green"      Main Menu"$cleard
	echo "[====================]"
	echo " 1. OS Info" ; sleep .125
	echo " 2. Network Info" ; sleep .125
	echo " 3. User's Information" ; sleep .125
	echo " 4. File Operations" ; sleep .125
	echo " 5. Find Files" ; sleep .125
	echo " 6. Exit" ; sleep .125
	sleep 1
	echo -e $blue" Enter your choice below [1-6]"$cleard

	read response

	case $response in

		1)
			echo "[====================]"
			echo -e $green"   OS System Info"$cleard
			echo "[====================]"
			echo " 1. Type of OS (Distrobution)"
			echo " 2. Free and used memory (RAM)"
			echo " 3. Disk usage (Hard Drive Info)"
			echo " 4. System Uptime"
			echo " 5. Back"
			read os_response
			case $os_response in
				1)
					echo "Type of OS (Distrobution)"
					#code
					echo
					cat /etc/os-release
					;;
				2)
					echo "Free and used memory (RAM)"
					#code
					free -th
					;;
				3)
					echo "Disk usage (Hard Drive Info)"
					#code
					df -Th
					;;
				4)
					echo "System Uptime"
					#code
					uptime -p
					;;
				5)
					echo "Exiting"
					;;
				*)
					echo "Invalid input, please select from the menu"
					;;
			esac
			;;
		2)
			echo "[====================]"
			echo -e $green " Network Information"$cleard
			echo "[====================]"
			echo " 1. List Network interfaces(ip command)"
			echo " 2. Network interface table (netstat)"
			echo " 3. Back"
			read network_response
			case $network_response in
				1)
					echo "List Network interfaces(ip command)"
					ip link show
					;;
				2)
					echo "Network interface table (netstat)"
					netstat -i
					;;
				3)
					echo "Exiting"
					;;
				*)
					echo "Invalid input, please select from the menu"
					;;
			esac
			;;

		3)
			echo "[====================]"
			echo -e $green"      User Info"$cleard
			echo "[====================]"
			echo " 1. Current users online"
			echo " 2. Last logged in user"
			echo " 3. Back"
			read user_info_response
			case $user_info_response in
				1)
					echo "Current users online"
					#code
					who -u
					;;
				2)
					echo "Last 10 logged in users on this system"
					#code
					last | tail
					;;
				3)
					echo "Exiting"
					;;
				*)
					echo "Invalid input, please select from the menu"
					;;
			esac
			;;
		4)
			echo "[====================]"
			echo -e $green"   File opperations"$cleard
			echo "[====================]"
			echo " 1. Create a file"
			echo " 2. Delete a file"
			echo " 3. Create a directory"
			echo " 4. Delete a directory"
			echo " 5. Compress a file"
			echo " 6. Decompress a file"
			echo " 7. Back"
			read file_opperations_response
			case $file_opperations_response in
				1)
					echo "Create a file"
					sleep 1
					echo "Please enter the file, extention and respective path you wish to create"
					#user enters a file path
					read file_create
					if ! [ -f $file_create ]
					then
						touch "$file_create"
						echo " $file_create was successfully created"

					else
						echo "$file_create already exists"
						echo "would you like to overwrite? [Y or N]"
						read create_ans

						if [ $create_ans = "Y" ] || [ $create_ans = "y" ]
						then 

							echo "Overwriting"
							touch "$file_create"

							
						else
							echo "Cancled"
							echo "$file_create was not overwritten"
						fi
					fi
					sleep 1
					;;
				2)
					echo "Delete a file"
					sleep 1
					echo "Please enter the file, extention and the respective path you wish to delete" 
					#user deletes a file via file path
					read file_delete
					rm $file_delete > /dev/null 2>&1
					if [ $? -eq 0 ]
					then
						echo "$file_delete was successfully deleted"
					else
						echo "no success in deleting $file_delete"
					fi
						
					;;
				3)
					echo "Create a Directory"
					sleep 1
					echo "Please enter the directory and respective path you wish to create"
					#user creates a directory and enters the directory name
					read dir_create
					mkdir $dir_create > /dev/null 2>&1
					if [ $? -eq 0 ]
					then
						echo "$dir_create was successfully created"
						echo "Would you like to edit its octal permissions? [Y or N]"
						read dircreate_ans
						if [ $dircreate_ans = "Y" ] || [ $dircreate_ans = "y" ]
						then
							echo "Enter the permissions you wish to set for the directory you've created"
							echo "in octal format"
							read dir_octal

							chmod $dir_octal $dir_create
							echo "octal permissions for $dir_octal have been set to $dir_octal"
						else
							echo "Directory permissons will not be modded"
						fi
					else
						echo "There was a problem with creating $dir_create so please try again"
					fi
					;;
				4)
					echo "Delete a Directory"
					sleep 1
					echo "Please enter the directory carefully, and its respective path you wish to delete"
					read dir_delete
					rmdir $dir_delete > /dev/null 2>&1
					if [ $? -eq 0 ]
					then
						echo "$dir_delete was successfully deleted"
						sleep .5
					else
						echo "Unable to delete $dir_delete successfully"
					fi

					#user deletes a directoy
					;;
				5)
					echo "Compress a file"
					sleep 1
					echo "Please enter the file you wish to compress including its absolute file path"
					echo "wild cards are also a valid search"
					echo "Example: test.txt, or *.txt"
					read compress_file

					gzip $compress_file

					if [ $? -eq 0 ]
                                        then
                                                echo "$compress_file was successfully compressed"
                                                sleep .5
                                        else
                                                echo "Unable to compress $compress_file successfully"
                                        fi



					#user compresses a specified file
					;;
				6)
					echo "Decompress a file"
					sleep 1
					echo "Please enter the compressed file including its absolute file path"
					echo "must be in .gz format"
					echo "Example: test.txt.gz, or bunnies.gz"
					read decompress_file
					gunzip $decompress_file

					if [ $? -eq 0 ]
                                        then
                                                echo "$decompress_file was successfully decompressed"
                                                sleep .5
                                        else
                                                echo "Unable to decompress $decompress_file successfully"
                                        fi
					#user de-compresses a file
					;;
				7)
					echo "Exiting"
					;;
				*)
					echo "Invalid input, please select from the menu"
					;;
			esac
			;;
		5)
			echo "[====================]"
			echo -e $green"     Find Files"$cleard
			echo "[====================]"
			echo " 1. Find files modded in the last x ammount of days"
			echo " 2. Find all files with specified extension"
			echo " 3. Back"
			read find_response
			case $find_response in
				1)
					echo "Find files that were modified in the last x ammount of days"
					sleep 1
					echo "Enter the time frame in which you would like to search in days ago"
					read search_time
					echo "now, enter the file you wish to search for"
					read search_file
					echo "Finding..."
					sleep 1
					find $search_file -type f -mtime -$search_time > /dev/null 2>&1
					if [ $? -eq 0 ]
                                        then
                                                echo " [ $search_file ] was successfully found"
                                                sleep .5
                                        else
                                                echo "Unable to find a modified $search_file successfully within the last $search_time days"
                                        fi


					#code
					;;
				2)
					echo "Find all files with specified extension"
					sleep 1
					echo "Enter the extention you would like to search all files within this directory for"
					read find_files

					find . -type f \( -name "*.$find_files" \)
					#code
					;;
				3)
					echo "Exiting"
					;;

				*)
					echo "Invalid input, please select from the menu"
					;;
			esac
			;;
		6)
			echo "Exiting..."
			sleep 2
			echo "Good-Bye"
			sleep .5
			exit
			;;
		*)
			echo "Invalid input, please select from the given menu"
			;;
	esac
done


#echo "[====================]"
#echo "      Main Menu"
#echo "[====================]"
#echo " 1. OS Info" ; sleep .125
#echo " 2. Network Info" ; sleep .125
#echo " 3. User's Information" ; sleep .125
#echo " 4. File Operations" ; sleep .125
#echo " 5. Find Files" ; sleep .125
#echo " 6. Exit" ; sleep .125
#sleep 1
#echo "Enter your choice below [1-6]" 


#read response
#case $response in
	

#while loop to run whilst menu is up waiting for a selection from the many "if" statements

	#case $response in
	
	#esac

	#keep looping untill an item is selected, I want to then end the command 
	#by having "i" increase by 1 to break the loop (preferably at an exit)
	#if [ $response -le 6 ]
	#then
		#if [ $response = 1 ]
		#then
			#echo "Success!!"
			#break
			##need to have it exicute then go back to menu status
			##goto command??? idk...

		#else
			#echo "still success, just not 1"
			##continue
			#break
		#fi
		##continue
	#else
		##stopping numbers from being selected outside the number range 
		#echo "Please select a number listed within the menu"

		#sleep 1

	#fi
#echo "Exiting"
#exit



#done
