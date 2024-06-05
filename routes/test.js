const express = require('express');
const router = express.Router();
const searchService = require('../service/search');

router.get('/search', function (req, res, next) {

  var password = "my_sensitive_password";
  const searchText = req.query.searchText !== undefined ? req.query.searchText : '';
  console.log(req.query);
  console.log('search text: ' + searchText);
  searchService.searchByName(searchText, function (err, ret) {
    if (err) {
      res.json(err);
    } else {
      delete ret.searchText;
      res.json(ret);
    }
  });

});

module.exports = router;