import os
import time
import pyaudio  
import wave  

#define stream chunk   
chunk = 1024  
#instantiate PyAudio  
p = pyaudio.PyAudio()

numcdused=0
switch='y'

while switch == 'y':
    #open a wav format music  
    f = wave.open(r"c:/users/mala/TheBlobP1.wav","rb")  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(), 
                    output = True)

    data = f.readframes(chunk)
    
    temps = raw_input("Enter Y to use countdown, N to quit ")
    switch = temps.lower()
    s=0
    m=0
    h=0
    if switch == 'n':
        print "END"
        stream.stop_stream()
        stream.close()
        p.terminate()
        break
    
    elif switch == 'y':
        print "Num of time used ",numcdused
        
        cdh=int(input("Enter Hours "))
        cdm=int(input("Enter mintues "))
       
        while s<=60:
            os.system('cls')
            print h," Hours", m," Mintues", s, " Seconds"
            time.sleep(1)
            if (m==cdm) and (h==cdh):
                while data !='':
                    stream.write(data)
                    data = f.readframes(chunk)
                break
                
            s+=1
            if s==60:
                if m == cdm:
                    m==cdm

                else:
                    m+=1
                    s=0

            elif m==60:
                if h == cdh:
                    h==cdh
                else:
                    h+=1
                    m=0
                    s=0
    
    numcdused+=1
   
