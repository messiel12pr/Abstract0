<template>
    <div>
        <pre id="editor"></pre>
    </div>
</template>
  
<script>
import '../../ace-builds/src-noconflict/ace.js';
import '../../ace-builds/src-noconflict/theme-dracula';
import '../../ace-builds/src-noconflict/mode-python';

export default {
    mounted() {
        // This hook is called after the component has been inserted into the DOM
        // and the editor element is available.

        // Initialize Ace editor
        const editor = ace.edit('editor');
        editor.setFontSize(25);
        editor.setShowPrintMargin(false);
        editor.setTheme('ace/theme/dracula');
        editor.session.setMode('ace/mode/python');
        editor.getSession().setUseWrapMode(true);

        // Retrieve content from local storage and set it in the editor
        const savedContent = localStorage.getItem('editorContent');
        if (savedContent) {
            editor.setValue(savedContent, 1);
        }

        // Update local storage whenever the editor content changes
        editor.on('change', () => {
            localStorage.setItem('editorContent', editor.getValue());
        });

        // You can store the editor instance in a data property if you need to
        this.editor = editor;
    },
};
</script>


<style scoped>
body {
    overflow: hidden;
    margin: 0;
    /* Remove default margin */
    background-color: #282A36
}

#editor {
    width: 65%;
    /* Set the desired width of the editor */
    height: 100%;
    /* Set the desired height of the editor */
    margin: 0;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
}
</style>