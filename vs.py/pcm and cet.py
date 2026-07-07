pcm=eval(input("Enter The PCM Score"))
cet=eval(input("Enter The CET Score"))
if(pcm>=150):
    if(cet>=100):
        print("Student is eligibel")
    else:
        print("Student is not eligibel")
else:
    print("Student is not eligibel")