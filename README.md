# ball-simulator
An elastic collision simulator built in Python using the Pygame library.

Allows the user to spawn bouncy balls, and also alter their elastic coefficient to determine how much velocity they keep after the bounce. The user can also
create super elastic collisions by raising the coefficent above 1, however this can quickly go out of control. Currently the collisions are not well optimized, 
and the simulator can reasonably only handle a few dozen balls. 

Plans:
* Create more newtonian physical elements for more accurate collisions
* Implement a binary search tree for collisions to reduce lag and improve collisions
* Add sliders and unique balls, in order to create a sandbox environment
