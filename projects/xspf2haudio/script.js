console.log("greetings from script.js");

function ui({ byId, elt, parseFromString, makeFileReader }) {
  const dropZone = byId("dropZone");

  // Optional.   Show the copy icon when dragging over.  Seems to only work for chrome.
  dropZone.addEventListener("dragover", function (e) {
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer.dropEffect = "copy";
  });

  // Get file data on drop
  const outElt = byId("out");
  dropZone.addEventListener("drop", function (e) {
    e.stopPropagation();
    e.preventDefault();
    var files = e.dataTransfer.files; // Array of all files

    for (var i = 0, file; (file = files[i]); i++) {
      if (file.type.match(/xspf/)) {
        var reader = makeFileReader();

        reader.onload = function (e2) {
          // finished reading file data.
          const xspf = e2.target.result;
          // document.body.appendChild(
          //  elt('pre', [xspf]));

          const plDoc = parseFromString(xspf, "text/xml");

          clear(outElt);
          const haudio = convert(plDoc, { elt });
          outElt.appendChild(haudio);
        };

        reader.readAsText(file); // start reading the file data.
      }
    }
  });
}

function convert(plDoc, { elt }) {
  const attr = (elt, n) => elt.querySelector(n).textContent;
  const tracks = Array.from(plDoc.querySelectorAll("track"));
  const toItem = (track) =>
    elt(
      "li",
      [
        elt("a", [elt("cite", [attr(track, "title")], { class: "fn" })], {
          href: attr(track, "location"),
          rel: "enclosure",
        }),
      ],
      { class: "item" }
    );
  return elt("ol", tracks.map(toItem), { class: "haudio" });
}

function clear(elt) {
  while (elt.hasChildNodes()) {
    elt.removeChild(elt.lastChild);
  }
}

function mkElt(document) {
  function elt(tag, children, attrs) {
    const e = document.createElement(tag); // AMBIENT global document
    e.append(...children);
    for (const a in attrs) {
      e.setAttribute(a, attrs[a]);
    }
    return e;
  }
  return elt;
}
