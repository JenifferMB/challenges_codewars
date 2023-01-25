package java.SmallestIntegerFinder;

/*

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
*/

public class SmallestIntegerFinder {
    public static int findSmallestInt(int[] args) {
      int aux = args[0];
      for(int i = 0; i < args.length; i++){
        if(args[i] < aux){
          aux = args[i];
          }
      }
      return aux;
    }
}

