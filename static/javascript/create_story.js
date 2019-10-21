function processForm()
{
  var temp = location.search.substring(1).split("&");
  const name = unescape(temp[0].split("=")[1].split('+').join(' '));
  const desc = unescape(temp[1].split("=")[1].split('+').join(' '))
  document.getElementById("name_of_story").innerText="Title: "+name;
  document.getElementById("des_of_story").innerText="Description: "+desc;
}
processForm();

document.querySelector('#story-card-submit').addEventListener('click', e => {
  let current_id = 0;
  if (document.getElementById("story-card").childNodes.length > 1){
    var children = document.getElementById("story-card").children;
    var last = children[children.length - 1];
    current_id = parseInt(last.id);
  }

  if (document.querySelector('#textarea-id').value) {
    const story_text = document.querySelector('#textarea-id').value;
    // const story_bookmark = document.querySelector('#bookmark').value;
    let body = document.createElement("p");
    body.className = "card-text"
    body.appendChild(document.createTextNode(story_text));

    let story = document.createElement("div");
    story.id = current_id+1;
    story.className = "card mb-2 border border-info col-12";


    document.querySelector("#story-card").appendChild(story);

    let small = document.createElement("small");
    small.className = "text-muted";
    small.appendChild(document.createTextNode(`Last updated ${document.lastModified}`));

    let date = document.createElement("p");
    date.className = "card-text";
    date.appendChild(small);

    let body_creator = document.createElement("div");
    body_creator.className = "card-body";
    body_creator.appendChild(body);
    body_creator.appendChild(date);
    story.appendChild(body_creator);
    

  }
  document.querySelector('#textarea-id').value = "";
  //prevents reloading/refreshing page
  e.preventDefault();
});
