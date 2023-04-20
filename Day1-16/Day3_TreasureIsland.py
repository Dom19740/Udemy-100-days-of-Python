print('''
                     _                 __                 
             __.--**"""**--...__..--**""""*-.            
           .'                                `-.         
         .'                         _           \        
        /                         .'        .    \   _._ 
       :                         :          :`*.  :-'.' ;
       ;    `                    ;          `.) \   /.-' 
       :     `                             ; ' -*   ;    
              :.    \           :       :  :        :    
        ;     ; `.   `.         ;     ` |  '             
        |         `.            `. -*"*\; /        :     
        |    :     /`-.           `.    \/`.'  _    `.   
        :    ;    :    `*-.__.-*""":`.   \ ;  'o` `. /   
              ;   ;                ;  \   ;:       ;:   ,/
         |  | |                    /  /`  | ,      `*-*'/ 
         `  : :  :                /  /    | : .    ._.-'  
          \  \ ,  \              :   `.   :  \ \   .'     
           :  *:   ;             :    |`*-'   `*+-*       
           `**-*`""               *---*                 
           '''
      )
print("\nWelcome to Treasure Island.")
print("\nYour mission is to find the treasure.")

choice1 = input("\nYou are standing at an entrance to a dark cave, type 'enter' to go in or 'around' to try and find a way around.\n").lower()

if choice1 == 'enter':
    choice2 = input('''\nOnce inside the cave you see two tunnels, type 'impailed' to go down the route with an impailed skeleton,
or type 'crushed' to go down the route that has a skeleton that looks like it was crushed by a boulder.\n''').lower()

    if choice2 == 'crushed':
        choice3 = input('''\nYou pass through the tunnel to find yourself in a vast cavern, type 'shout' to see if anyone is home,
type 'sneak' to explore quietly, or type 'think' to well.. think about it some more.\n''').lower()
        
        if choice3 == 'sneak':
            print("\nYou sneak past a herd of sleeping ancient rhinos, and find the treasure. Good Job... YOU WON!! F**k Dem Rhinos!!\n")
        elif choice3 == 'shout':
            print("\nYou wake up a sleeping herd of ancient rhinos that were guarding the treasure, and are trampled to death. Game Over!\n")
        else: 
            print("\nYou got slowly munched upon by a herd of ancient rhinos and died because of procrastination, pfff. Game Over!!\n")
    else:
        print("\nYou were impailed by some spikes that came out of the wall, the skeleton should have been a clue. Game Over!\n")
else:
    print("\nYou tried to climb around the entrance to the cave but got stuck in a large pile of what could be rhino poo, and you died. Game Over!!\n")
