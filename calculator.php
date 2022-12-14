<?php

class calculator{
    public function add($num1,$num2){
        print  $num1+$num2;
        
    }
    public function sub($num1,$num2){
        print  $num1-$num2;

    }
    public function multiple($num1,$num2){
        print  $num1*$num2;
    }
    public function divide($num1,$num2){
        print $num1/$num2;
    }
}
$calculator= new calculator();

$num1=readline("Enter number1:");
$num2=readline("Enter number2:");
$input=readline("What kind of opearation do you wat to execute +,-,*,/:");

switch ($input) {
    case '+':
            $calculator:: add($num1,$num2);
        break;
    case '-':
            $calculator:: sub($num1,$num2);
        break;
    case '*':
            $calculator:: multiple($num1,$num2);
        break;
    case '/':
            $calculator:: divide($num1,$num2);
        break;
    
    default:
        print "please give a valid input";
        break;
}





?>
