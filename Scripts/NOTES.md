## Things you can do some things you can't
Can't use giant decoration as a sky box because it gets culled


Yes, exactly. The line of sight represents the direction in which the camera is facing. In a 3D environment, it's often represented as a vector starting from the camera's position and extending outward in the direction the camera is pointed.

So, if you have the coordinates of the camera and you calculate the line of sight using trigonometric calculations based on the camera's rotation angles, the resulting point represents where the camera is facing or what it's looking at in the scene. It's essentially the point in 3D space that the camera's lens is pointed towards.

Somewhat continuous rock paper scissors where you try to predict the Distribution that will defeat the opponent but in this case it'll only be three numbers so it'll be like a triangle and you have to predict the distribution that will defeat the opponents distribution.


if $global.playerIsSneaking == 1 {

} 
if $global.pStatePushBack == 1 {
//Need to find the player's current angle to find the opposite force to push
}

if $global.pStateSlowed == 1 {
player speed 125
}else{
player speed 250
}

if $global.pStateQuickend == 1 {
player speed 275
}else{
player speed 250
}



//get ||v|| = sqrt(x^2 + y^2 + z^2)
v = $global.playerXNorm
v+=$global.playerYNorm
v+=$global.playerZNorm

//Apparently you can choose any positive value as an initial guess and by any I'm assuming even numbers that go above the square Approximation. So I'm gonna take the average to get close as I can to try and save on calculations

avg = $global.playerX
avg+=$global.playerY
avg+=$global.playerZ

avg/=3

//Make an initial guess. Guess any positive number x0.
//Improve the guess. Apply the formula x1 = (x0 + S / x0) / 2. The number x1 is a better approximation to sqrt(S).
//Iterate until convergence. Apply the formula xn+1 = (xn + S / xn) / 2 until the process converges. Convergence is achieved when the digits of xn+1 and xn agree to as many decimal places as you desire.

s = $v
tmp = 0
x1 = 0
x2 = 0
x3 = 0

//(x0 + v / x0)/2
x0 = $avg 
tmp+=$v
tmp/=$x0
x0+=$tmp
x1+=x0
x1/=2

//(x1 + v / x1)/2
tmp = 0
tmp+=$v
tmp/=$x1
x1+=$tmp
x2+=x1
x2/=2

//(x2 + v / x2)/2
tmp = 0
tmp+=$v
tmp/=$x2
x2+=$tmp
x3+=x2
x3/=2

status "x0 $x0, x1 $x1, x2 $x2, x3 $x3"
//Update at last so it still has the same value the next time comes around
player check position global.lastX global.lastY global.lastZ
end
//status "$map.test_chase"

//Find player vector and normalize it and set it to global.playerXNorm, global.playerYNorm global.playerZNorm




procedure sqrtEstimate
//Babylonian square-root algorithm
//sqrtEstimate (global.arg0 ,global.arg1, global.arg2) ->global.funcResult
//              S           ,x0          ,iterations
if $global.arg2 > 0 {
global.arg2--
tmp=0
//(x0 + S / x0)/2
tmp+=$global.arg0
tmp/=$global.arg1
tmp+=$global.arg0
tmp/=2

global.arg1*=0
global.arg1+=$tmp

call sqrtEstimate
} else {
global.funcResult = $global.arg1
} 
end;







//S=v, x0=avg, iterations=10
//First I have to clear out the global variables
global.arg0*=0
global.arg1*=0
global.arg2*=0
global.funcResult*=0

//Let's load the Variables
global.arg0+=$v
global.arg1+=$avg
global.arg2+=3

//call sqrtEstimate
//status $global.funcResult 1







