function show_More_1() {
  var dots_1 = document.getElementById("dots_1");
  var moreText_1 = document.getElementById("more_1");
  var btnText_1 = document.getElementById("studentButton");

 if (dots_1.style.display === "none") {
    dots_1.style.display = "inline";
    btnText_1.innerHTML = "Read more";
    moreText_1.style.display = "none";
  } else {
    dots_1.style.display = "none";
    btnText_1.innerHTML = "Read less";
    moreText_1.style.display = "inline";
  }
}

function show_More_2() {
  var dots_2 = document.getElementById("dots_2");
  var moreText_2 = document.getElementById("more_2");
  var btnText_2 = document.getElementById("teacherButton");
 
  if (dots_2.style.display === "none") {
    dots_2.style.display = "inline";
    btnText_2.innerHTML = "Read more";
    moreText_2.style.display = "none";
  } else {
    dots_2.style.display = "none";
    btnText_2.innerHTML = "Read less";
    moreText_2.style.display = "inline";
  }
}

function show_More_3() {
  var dots_3 = document.getElementById("dots_3");
  var moreText_3 = document.getElementById("more_3");
  var btnText_3 = document.getElementById("parentButton");

  if (dots_3.style.display === "none") {
    dots_3.style.display = "inline";
    btnText_3.innerHTML = "Read more";
    moreText_3.style.display = "none";
  } else {
    dots_3.style.display = "none";
    btnText_3.innerHTML = "Read less";
    moreText_3.style.display = "inline";
  }
}