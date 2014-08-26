import zipfile,sys,time
import itertools
import rarfile
def extractFile(zFile, password,ext):
    if ext == "zip":
        return extrat_zip(zFile,password)
    elif ext == "rar":
        return extrat_rar(zFile,password)        
def extrat_rar(rfile,password):
    try:
        rfile.extractall(pwd=password)
        print ' Found password : ', password
        return True
    except:
        return False    

def extrat_zip(zfile,password):
    try:
        answer= zfile.extractall(pwd=password)
        print ' Found password : ', password
        return True
    except:
        #print password + " was incorrect"
        return False   

def main(ifile):
    ext = ifile.split('.')[-1]
    if ext == 'rar':
         zFile= rarfile.RarFile(ifile)

    elif ext == "zip":   
         zFile = zipfile.ZipFile(ifile)
    else:
        print "invalid file"
        sys.exit()    
    #open(fname, mode='r', psw=None)
    pass_str = "abcdebcdefghijklmnopqrstuvwxyz0123456789"
    for pass_len in range(1,5):
        passwords = itertools.permutations(pass_str,pass_len)
        for password in passwords:
            #print password
            #time.sleep(.01)
            password = ''.join(password)
            sys.stdout.write("\r checking .. %s" % password )
            sys.stdout.flush()

            if (extractFile(zFile, password,ext)):
                print "checked  "+password+"  ..."
                sys.exit()

if __name__ == '__main__':
    try:
        ifile = sys.argv[1]
    except:
        print "please run like  'zip.exe inputfilename'"
        sys.exit()    
    main(ifile)