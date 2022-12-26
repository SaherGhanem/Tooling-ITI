#/*****************************************************************************/
#/*****************************************************************************/
#/**************************		Author: SAHER GHANEM 	    *********************/
#/**************************		   ITI-INTAKE43           *********************/
#/**************************		     Tooling              *********************/
#/**************************		    File-Lab              *********************/
#/**************************		   Version:1.00 	        *********************/
#/**************************		DATE: 12/19/2022         	*********************/
#/*****************************************************************************/
#/*****************************************************************************/

import sys,os

#Write a function named countEndWrd that takes 2 arguments filename and word.
#Count how many times the given word appears at the end of a line, 
#Then append the following string to the passed file : 
#'The word => '+"'"+word+"'"+' appears => '+count+' times' .
'''
Write your function Here
'''
def countEndWrd(filename,word):
  
  count = 0
  with open(filename, 'r') as f:
      for i in f:
        if i.endswith(word+'\n'):
          count=count+1
  f.close()
  f=open(filename, 'a')
  string='The word => '+"'"+word+"'"+' appears => '+str(count)+' times'
  f.write(string)
  f.close()
  

      
  
  
    
  



#Write a function named copyWrdToFile that takes 2 arguments source_file and word.
#It should copy all lines that contain the passed word from the file source_file 
#to a new file named 'new_file.txt'. 


#Provided function to test your solution.  
def testAll():
  f=open('countEndWrd.txt','r')
  temp_list=f.readlines()
  if temp_list[len(temp_list)-1] == "The word => 'END' appears => 2 times":
    print ('countEndWrd=OK')
  else:
    print ('countEndWrd=NOK')
  f.close()
  
  if os.path.exists('new_file.txt'):
    f=open('new_file.txt','r')
    temp_list=f.readlines()
    f.close()
    if len(temp_list) == 3:
      if temp_list[0] =='A person can live without food for about a'\
      +' month, but only about a week without water.\n' and temp_list[1]\
      == 'Gopher snakes in Arizona are not poisonous, but when frightened'\
      +' they may hiss and shake their tails like rattlesnakes.\n' and temp_list[2]\
      == 'Cats sleep up to eighteen hours a day, but never'\
      +' quite as deep as humans. Instead, they fall asleep quickly and '\
      +'wake up intermittently to check to see if their environment is still safe.\n': 
        print ('copyWrdToFile=OK')
      else:
        print ('copyWrdToFile=NOK')
    else:
      print ('copyWrdToFile=NOK')
  else:
    print ('copyWrdToFile=NOK')

def main():
  countEndWrd('countEndWrd.txt','END')
 # copyWrdToFile('copyWrdToFile.txt','but')
  testAll()

if __name__ == '__main__':
  main()  

  