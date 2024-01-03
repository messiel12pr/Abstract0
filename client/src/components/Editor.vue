<template>
    <div>
        <pre id="editor"></pre>
        <button type="button" @click="submitCode" id="submitButton" class="btn btn-submit btn-lg">Submit</button>
    </div>
</template>
  
<script>
import '../../ace-builds/src-noconflict/ace.js';
import '../../ace-builds/src-noconflict/theme-one_dark';
import '../../ace-builds/src-noconflict/mode-python';
import axios from 'axios';

export default {
    mounted() {
        // This hook is called after the component has been inserted into the DOM
        // and the editor element is available.

        // Initialize Ace editor
        const editor = ace.edit('editor');
        editor.setFontSize(25);
        editor.setShowPrintMargin(false);
        editor.setTheme('ace/theme/one_dark');
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
    data() {
        return {
            submissionResult: '',
        };
    },
    methods: {
        submitCode() {
            const path = 'http://localhost:5001/submit';
            var mode = this.editor.session.$modeId
            mode = mode.substr(mode.lastIndexOf('/') + 1);

            const requestData = {
                language: mode,
                code: this.editor.session.getValue(),
            };

            axios.post(path, requestData)
                .then((res) => {
                    this.submissionResult = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
            console.log(this.submissionResult)
        },
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
    height: 98%;
    /* Set the desired height of the editor */
    margin: 12px;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    border-radius: 10px;
}

#submitButton {
    position: absolute;
    top: 94%;
    /* Adjust top position as needed */
    left: 66%;
    /* Adjust left position as needed */
    z-index: 1;
    /* Set a higher z-index to ensure it appears above #editor */
    color: #282A36;
    border-color: black;
    background-color: #F1FA8C;
    padding: 8px 50px;
}
</style>