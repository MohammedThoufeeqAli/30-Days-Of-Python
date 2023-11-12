coins=int(input("Enter the No. of Gold Coins : ")) 
friend_1=int(input("Enter the Share of Your First Friend : ")) 
friend_2=int(input("Enter the Share of Your Second Friend : "))
friend_3=int(input("Enter the Share of Your Third Friend : ")) 

if (friend_1>0) and (friend_2>0) and (friend_3>0) :

    if (friend_1!=friend_2) and (friend_2!=friend_3) and (friend_3!=friend_1) :
     
        if(friend_1+friend_2+friend_3 == coins) :
            print("\nFAIR")
       
        else:
            print("\nUNFAIR")
    else:
            print("\nUNFAIR")        
else:
            print("\nUNFAIR")