<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Basic for loop example</title>
    <style>

    </style>
  </head>
  <body>
  <p></p>
    <script>
    function guessNumber() {
      // Get a random integer from 1 to 10 inclusive
      var num = Math.ceil(Math.random() * 10);
      var guess;

      while (guess != num) {
        guess = prompt('Guess the number between 1 and 10 inclusive');
      }
      alert('Congratulations!\nThe number was ' + num);
    }

    guessNumber();
    </script>
  </body>
</html>
