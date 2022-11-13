# Text-Based mini–Pokémon Game

### ITE1015 Creative Software Design 
### Department of Data Science 
### Hanyang University

<br>

## Pokémon Battle
- Let’s make a text-based Pokémon game via python.
    - https://www.youtube.com/watch?v=1hvTGrt87Sc
    - https://www.youtube.com/watch?v=dxhtGqcds2Q
- Your goal is to become a Pokémon master!
- You have 3 steps left to become a Pokémon master, 
Let’s choose your Pokémon among 3 of Pokémons and take a 
walk!

## Game Order
1. Set the trainer’s name
2. Choose the starter Pokémon among (Charmander, Bulbasaur, Squirtle)
3. Set the name of Pokémon you choose
4. Trainer’s goal is to become a Pokémon master, to achieve his/her dream, trainer has 3 steps left to Pokémon master.
5. Trainer can choose 4 ways to walk, each of east, west, north, south.
6. Each of the wild Pokémon (Charmander, Bulbasaur, Squirtle, and None) is assigned randomly to each way (no duplicates).
    1. If the path Trainer choose was None, Trainer doesn’t need to fight wild Pokémon but just walk 1 step.
    2. Otherwise, if the Trainer choose was encountering wild Pokémon, then Pokémon battle starts.
7. Pokémon battle finished when either HP of enemy or my Pokémon is 0 (HP cannot be negative) 
    1. If Trainer has no Pokémon left to fight, game is over
    -> print “{Trainer’s name} Blacked out!”
    2. If Trainer has Pokémon left alive to fight, Trainer can choose Pokémon among them
8. Every battle starts with the action of the Trainer, Trainer has 5 options below:
    1. Elemental attack
        - attack wild Pokémon with each Pokémon’s own elemental attack
        - damage 2x if (attack from attribute: Fire àGrass, Grass àWater, Water àFire)
        - damage 0.5x vice versa (attack from attribute: Grass àFire, Water àGrass, Fire àWater)
    2. Physical attack
        - ‘Tackle’ enemy Pokémon
        - deals equivalent of 10 damage no matter what enemy’s attribute is
    3. Cure
        - heal maximum of your Pokémon on the battleground
    4. Capture wild Pokémon
        - 90% of success possibility if wild Pokémon’s HP is under 50% of maxHP
        - 10% of success possibility if wild Pokémon’s HP is over or equal to 50% of maxHP
        - if your capturing is missed, your turn finished
    5. Change Pokémon in my hands
        - choose another Pokémon among your Pokémon in hands.
        - if you have just 1 Pokémon only, you cannot choose this option (if player choose this option even if player just has only 1 Pokémon, send alert message)
        - if player’s Pokémon’s HP becomes 0, then that Pokémon is dead, and trainer throw that monster ball away
9. After the turn of trainer is finished, wild Pokémon use only elemental attack to attack Trainer’s Pokémon.
10. After each of Pokémon’s turn is over, information of HP left of my Pokémon and wild Pokémon should be printed on  python shell
11. After trainer complete his/her 3 steps of walking, print the word “{trainer’s name}! Congratulations! You became Pokémon  master!”