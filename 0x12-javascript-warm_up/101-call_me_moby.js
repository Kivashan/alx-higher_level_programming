#!/usr/bin/node

exports.callMeMoby = function (a, b) {
  for (a; a > 0; a--) {
    b();
  }
};
