# CEN4020GroupProject
-Group members:
  -Alexander Jordan
  -Anthony Micciche
  -Alexander Kostandarithes
  -Ryan Goldberg
  -Karl Cooley

  -Project ideas:
    -some sort of game, maybe an rpg
    -post relevant gameplay/storyline ideas here:
        -<gameplay ideas>
    -Assuming 2d gameplay we need to find a language/framework that will work well:
      -python has a pretty cool game design library called arcade, I think this could be a good option
      -post other possible ideas/frameworks to use here:
        -<framework ideas>
   -Also need to come up with a title for the game to turn in monday 25th of may:
      -<title ideas>

-Discussion
-If you guys want to figure out the inner-workings of how games run, using Python is fine. However, depending on the scope of the game I wouldn't really recommend it. I used pygames (arcade may be different) for a class project (https://github.com/jeffmanassa97/StarCraftLikeGame/tree/master/Scuffed%20Starcraft) and it was kind of a pain. The pygame library only seemed to help us with rendering (game layers: overlay, units, and background), but you have to implement everything else yourself. I worked on UI and that involved me drawing rectangles all over the display pixel by pixel. You have to create your own buttons using the input library and use your defined rectangles (see overlay file if interested) to create input events. I'm not familiar with other game making frameworks, so I'm not really sure if they are better.
--Karl
