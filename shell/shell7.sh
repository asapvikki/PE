#!/bin/bash
echo "first side"
read side1
echo "second side"
read side2
echo "third side"
read side3

if [ [$side1 -eq $side2] ]&& [ [$side2 -eq $side3]  ]
then echo "equilateral"
elif [ [$side1 -eq $side2] ]
then echo "isosceles"
elif [ [$side2 -eq $side3] ]
then echo "isosceles"
elif [ [$side3 -eq $side1 ] ]
then echo "isosceles"
else echo "scalene"
fi
