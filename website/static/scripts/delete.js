function deleteNote(noteId) {
    fetch("/delete", {
      method: "DELETE",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = `/`; 
    });
  }
