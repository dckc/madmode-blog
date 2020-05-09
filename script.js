console.log('greetings from script.js');


var dropZone = document.getElementById('dropZone');

// Optional.   Show the copy icon when dragging over.  Seems to only work for chrome.
dropZone.addEventListener('dragover', function(e) {
    e.stopPropagation();
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
});


function elt(tag, children, attrs) {
    const e = document.createElement(tag); // AMBIENT global document
    e.append(...children);
    for (const a in attrs) {
	 e.setAttribute(a, attrs[a]);
    }
    return e;
}


// Get file data on drop
dropZone.addEventListener('drop', function(e) {
    e.stopPropagation();
    e.preventDefault();
    var files = e.dataTransfer.files; // Array of all files

    for (var i=0, file; file=files[i]; i++) {
        if (file.type.match(/xspf/)) {
            var reader = new FileReader();

            reader.onload = function(e2) {
                // finished reading file data.
                const xspf = e2.target.result;
                // document.body.appendChild(
                //  elt('pre', [xspf]));

                const plDoc = ( new window.DOMParser() ).parseFromString(xspf, "text/xml");
                const attr = (elt, n) => elt.querySelector(n).textContent;
                const tracks = Array.from(plDoc.querySelectorAll('track'));
                const toItem = track => elt('li', [
                  elt('a', [elt('cite', [attr(track, 'title')],
                   {class: 'fn'})],
                      {href: attr(track, 'location'), rel: 'enclosure'})
                ], {class: 'item'});
                const outElt = document.getElementById('out');
                while (outElt.hasChildNodes()) {
                  outElt.removeChild(outElt.lastChild);
                }
                out.appendChild(elt('ol', tracks.map(toItem),
                 {class: 'haudio'}));
            }

            reader.readAsText(file); // start reading the file data.
        }
    }
});
