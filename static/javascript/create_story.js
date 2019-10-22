function removeBookmark(e){
  e = e || window.event;
  e = e.target || e.srcElement;
  hash = e.id;
  alert(e.id)
  card = document.getElementById("cardhashedId"+hash)
  card.parentNode.removeChild(card)
}

function renderBookmark(e) {
  e = e || window.event;
  e = e.target || e.srcElement;
  bookmarkId = e.value
   document.getElementById("select-default").selected = "selected"
  fetch("http://localhost:8000/bookmarks/" + bookmarkId+"/", {
      method: "GET",
      headers: {
          'X-CSRFToken': csrf,
          'content-type': 'application/json'
      }
  }).then(res => res.json())
  .then(data => {
    let current_id = 5;
    if (document.getElementById("story").children.length > 5){
      var children = document.getElementById("story").children;
      alert(children.length)
      var last = document.getElementById(children.length-1);
      current_id = parseInt(last.id)+1;
    }
    story = document.getElementById("story")
    bookmark = addCard(data, current_id);
    story.appendChild(bookmark)
    newBookmark = document.getElementById("hashedId" + current_id)
    newBookmark.name = "bookmark"+data.id
    newBookmark.id = current_id
    newBookmark.classList.add("btn-warning");
    newBookmark.classList.remove("btn-danger")
    newBookmark.innerHTML = "remove"
    newBookmark.removeEventListener('click', deleteBookmark);
    newBookmark.addEventListener("click", removeBookmark);

    newContentButton = document.getElementById("content-button"+"hashedId" + current_id)
    newContentButton.id = "content-button" + current_id
    newContentButton.href = "#content" + current_id
    newContentButton.setAttribute("aria-controls", "content" + current_id)

    newContent = document.getElementById("content"+"hashedId" + current_id)
    newContent.id = "content" + current_id

    newContentBody = document.getElementById("content-body"+"hashedId" + current_id)
    newContentBody.id = "content-body" + current_id
  });


}

document.querySelector('#story-card-submit').addEventListener('click', e => {
  let current_id = 0;
  if (document.getElementById("story-card").childNodes.length > 1){
    var children = document.getElementById("story-card").children;
    var last = children[children.length - 1];
    current_id = parseInt(last.id);
  }
  if (document.querySelector('#editor').value) {
    const story_text = document.querySelector('#editor').value;
    let body = document.createElement("p");
    body.className = "card-text"
    body.appendChild(document.createTextNode(story_text));

    let story = document.createElement("div");
    // story.id = current_id+1;
    story.className = "card mb-2 border border-info col-12";




    let small = document.createElement("small");
    small.className = "text-muted";
    small.appendChild(document.createTextNode(`Last updated ${document.lastModified}`));

    let date = document.createElement("p");
    date.className = "card-text";
    date.appendChild(small);

    let body_creator = document.createElement("div");
    body_creator.className = "card-body";
    body_creator.appendChild(body);
    // body_creator.appendChild(date);
    story.appendChild(body_creator);

    let edit = document.createElement("button");
    edit.className = "btn btn-outline-primary btn-sm mr-1";
    edit.innerText = "Edit"

    let remove = document.createElement("button");
    remove.className = "btn btn-outline-primary btn-sm mr-1";
    remove.innerText = "Remove"

    let bottom = document.createElement("div");
    bottom.className = "card-img-bottom pb-2";
    bottom.appendChild(edit)
    bottom.appendChild(remove)
    story.appendChild(bottom)

    document.querySelector("#story").appendChild(story);
    // document.querySelector("#story").appentChild(storyCard)

  }
  document.querySelector('#editor').value = "";
  //prevents reloading/refreshing page
  e.preventDefault();
});
