import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "fingerprint_enhancer"])
import fingerprint_enhancer, cv2

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        image_name = sys.argv[1]
        img = cv2.imread('Unenhanced Images/'+image_name+'.jpg', 0)						# read input image
        out = fingerprint_enhancer.enhance_Fingerprint(img)		# enhance the fingerprint image
        
        cv2.imwrite('Images/'+image_name+'.jpg', out)