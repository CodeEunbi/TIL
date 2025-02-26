s<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <style>
    .box {
        width: 200px;
        height: 200px;
    }

    .box-container {
        width: 300px;
    }
    /* .be-success {
        background-color: green;
    } */
  </style>
</head>

<body>
  <h1>Hello Bootstrap!!</h1>
  <h2>Heading 2</h2>

  <div class="box bg-primary rounded-4">a box</div>
  <div class="box-container m-3 p-4 border border-3 border-dark rounded-3 bg-secondary">
    <div class="box mx-auto mb-3 bg-success rounded-circle"></div>
    <div class="box mx-auto mb-3 bg-warning rounded-circle"></div>
    <div class="box mx-auto bg-danger rounded-circle"></div>
  </div>


  <div class="d.flex border border-3 border-dark rounded-3 justify-content-evenly">
    <div class="box bg-success rounded-circle"></div>
    <div class="box bg-warning rounded-circle"></div>
    <div class="box bg-danger rounded-circle"></div>

  </div>


  <!-- <div class="box bg-success rounded-circle"></div>
  <div class="box bg-warning rounded-circle"></div>
   <div class="box bg-danger rounded-circle"></div> -->

  <!--bootstrap js 적용하기-->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <!-- <script src = "js/bootstrap.js></script>" -->
</body>

</html>
