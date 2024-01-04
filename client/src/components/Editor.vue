<template>
    <div>
        <pre id="editor"></pre>
        <button type="button" :disabled="isButtonDisabled" @click="submitCode()" id="submitButton"
            class="btn btn-submit btn-lg">Submit</button>
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
        <div id="submission-container">
            <h4>Submission Details</h4>
            <div id="submission-details" v-if="state.submission">
                <ul>
                    <li>Result: {{ state.submissionResult }}</li>
                    <li>Standard Output: {{ state.stdout }}</li>
                    <li>Expected Output: {{ state.expectedOutput }}</li>
                </ul>

            </div>
            <div v-else>Hang in there, code is on its way...</div>
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

        const editor = ace.edit('editor');
        editor.setFontSize(25);
        editor.setShowPrintMargin(false);
        editor.setTheme('ace/theme/one_dark');
        editor.session.setMode(this.state.language);
        editor.getSession().setUseWrapMode(true);
        editor.setValue(this.state.user_input, 1);

        editor.on('change', () => {
            this.state.user_input = editor.getValue();
        });

        this.editor = editor;
    },

    data() {
        return {
            state: {
                language: localStorage.getItem('editorLanguage') || 'ace/mode/python',
                user_input: localStorage.getItem('editorContent') || '',
                submission: false,
                submissionResult: '',
                stdout: '',
                expectedOutput: '',
            },
            isButtonDisabled: false,
        };
    },

    methods: {
        submitCode() {
            this.isButtonDisabled = true;
            const path = 'http://localhost:5001/submit';
            var mode = this.editor.session.$modeId
            mode = mode.substr(mode.lastIndexOf('/') + 1);

            const requestData = {
                language: mode,
                code: this.state.user_input,
            };

            axios.post(path, requestData)
                .then((res) => {
                    this.state.submission = true;
                    this.state.submissionResult = res.data.status.description
                    this.state.stdout = atob(res.data.stdout)
                    this.state.expectedOutput = atob(res.data.expectedOutput)
                })
                .catch((error) => {
                    console.error(error.data);
                    this.isButtonDisabled = false;
                });

        },

        handleDropdownItemClick(language) {
            this.state.language = language;
            this.editor.session.setMode(language);
        },

        handleBeforeUnload() {
            // Save the state to localStorage just before the page is unloaded
            localStorage.setItem('editorLanguage', this.state.language);
            localStorage.setItem('editorContent', this.state.user_input);
            // Save submission data in db
        },
    },

    beforeUnmount() {
        window.removeEventListener('beforeunload', this.handleBeforeUnload);
    },

    created() {
        window.addEventListener('beforeunload', this.handleBeforeUnload);
    },
};
</script>


<style scoped>
#editor {
    width: 65%;
    height: 97%;
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

#submission-container {
    overflow: hidden;
    background-color: #e4e6eb;
    width: 32%;
    height: 15%;
    position: absolute;
    top: 74.5%;
    margin: 0 auto;
    left: 67%;
    border-radius: 1.5%;
    text-align: center;
}

#submission-details {
    text-align: left;
}
</style>