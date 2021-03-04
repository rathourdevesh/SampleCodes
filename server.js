console.log("server ");

var express = require('express');
var morgan = require('morgan');
var path = require('path');

var app = express();
app.use(morgan('combined'));

app.get('/', function(req,res){
   res.send('Hello');
});

var port = 8080;
app.listen(port, function () {
  console.log(`listening on port ${port}!`);
});
