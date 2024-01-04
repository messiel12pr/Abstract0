<template>
    <div>
        <pre id="editor"></pre>
        <button type="button" @click="submitCode" id="submitButton" class="btn btn-submit btn-lg">Submit</button>
        <div id="dropdown-container" class="dropup">
            <button id="language-dropdown" class="btn btn-custom dropdown-toggle btn-lg" type="button"
                data-bs-toggle="dropdown" aria-expanded="false">
                Language
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                <li><a class="dropdown-item" href="#" @click="handleDropdownItemClick('ace/mode/c_cpp')">C++</a></li>
                <li><a class="dropdown-item" href="#" @click="handleDropdownItemClick('ace/mode/python')">Python</a></li>
                <li><a class="dropdown-item" href="#" @click="handleDropdownItemClick('ace/mode/java')">Java</a>
                </li>
            </ul>
        </div>
    </div>
</template>
  
<script>
import '../../ace-builds/src-noconflict/ace.js';
import '../../ace-builds/src-noconflict/theme-one_dark';
import '../../ace-builds/src-noconflict/mode-c_cpp';
import '../../ace-builds/src-noconflict/mode-python';
import '../../ace-builds/src-noconflict/mode-java';
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
                    this.submissionResult = res;
                    console.log(res.data.status.description)
                    console.log(atob(res.data.stdout))
                    console.log(atob(res.data.expected_output))
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        handleDropdownItemClick(language) {
            this.editor.session.setMode(language);
        }
    },
};
</script>


<style scoped>
#editor {
    width: 65%;
    /* Set the desired width of the editor */
    height: 97%;
    /* Set the desired height of the editor */
    margin: 0.9%;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 1% 3%;
    border-radius: 1.5%;
}

#submitButton {
    position: absolute;
    top: 91.5%;
    margin: 0%;
    left: 67%;
    z-index: 1%;
    color: #282A36;
    border-color: black;
    background-color: #F1FA8C;
    font-size: 1vw;
    width: 10vw;
    height: 7vh;
}

#dropdown-container {
    position: absolute;
    top: 91.5%;
    margin: 0%;
    left: 78%;
    z-index: 1%;
}

.btn-custom {
    color: #282A36;
    border-color: black;
    background-color: #F1FA8C;
    font-size: 1vw;
    width: 21vw;
    height: 7vh;
}

.dropdown-item {
    color: #282A36;
    width: 21vw;
    font-size: 1rem;
}

.dropdown-menu {
    background-color: #e4e6eb;
}
</style>