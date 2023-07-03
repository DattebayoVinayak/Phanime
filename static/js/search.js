

function nextPage(e){
  let index = Number(document.querySelector(".index").innerHTML);
  if(window.location.href.includes(`&page=${index}`)){
  window.location.href = window.location.href.replace(`&page=${index}`,`&page=${Number(index)+1}`)
  }else if(!(window.location.href.includes(`&page=${index}`))){
    window.location.href = window.location.href+`&page=${Number(index)+1}`
}
}

function prevPage(e){
  let index = Number(document.querySelector(".index").innerHTML);
  if(window.location.href.includes(`&page=${index}`)){
    window.location.href = window.location.href.replace(`&page=${index}`,`&page=${Number(index)-1}`)
    }else if(!(window.location.href.includes(`&page=${index}`))){
      window.location.href = window.location.href+`&page=${Number(index)-1}`
  }
}