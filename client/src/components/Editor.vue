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
import { ref, reactive, watch, onMounted, onBeforeUnmount } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';

export default {
    setup() {
        const { isAuthenticated, getAccessTokenSilently } = useAuth0();

        const state = reactive({
            language: localStorage.getItem('editorLanguage') || 'ace/mode/python',
            user_input: localStorage.getItem('editorContent') || '',
            submission: false,
            submissionResult: '',
            stdout: '',
            expectedOutput: '',
        },)

        const editor = reactive({
            instance: null,
        });

        const isButtonDisabled = ref(false);

        onMounted(() => {
            window.addEventListener('beforeunload', handleBeforeUnload);
            const aceEditor = ace.edit('editor');
            aceEditor.setFontSize(25);
            aceEditor.setShowPrintMargin(false);
            aceEditor.setTheme('ace/theme/one_dark');
            aceEditor.session.setMode(state.language);
            aceEditor.getSession().setUseWrapMode(true);
            aceEditor.setValue(state.user_input, 1);

            editor.instance = aceEditor;

            editor.instance.on('change', () => {
                state.user_input = editor.instance.getValue();
            });

            if (!isAuthenticated.value) {
                isButtonDisabled.value = true;
                alert("Log in, in order to submit code");
            }

            else
                isButtonDisabled.value = false;
        });

        onBeforeUnmount(() => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        });

        const handleBeforeUnload = () => {
            // Save the state to localStorage just before the page is unloaded
            localStorage.setItem('editorLanguage', state.language);
            localStorage.setItem('editorContent', state.user_input);
            // Save submission data in db
        }

        const getModeId = () => {
            if (editor.instance && editor.instance.session) {
                var mode = editor.instance.session.$modeId
                return mode.substr(mode.lastIndexOf('/') + 1);
            }
            else
                return null;
        }

        const submitCode = async () => {
            try {
                const token = await getAccessTokenSilently();
                isButtonDisabled.value = true;
                const path = 'http://localhost:5001/submit';
                const mode = getModeId();

                const requestData = {
                    language: mode,
                    code: state.user_input,
                };

                axios.post(path, requestData, { headers: { 'authorization': 'Bearer ' + token } })
                    .then((res) => {
                        state.submission = true;
                        state.submissionResult = res.data.status.description
                        state.stdout = atob(res.data.stdout)
                        state.expectedOutput = atob(res.data.expectedOutput)
                    })
                    .catch((error) => {
                        console.error(error.data);
                        isButtonDisabled.value = false;
                    });
            }
            catch (error) {
                if (error.message.split(' (')[0] == 'Missing Refresh Token')
                    alert("Log in, in order to submit code")
            }


        }

        const handleDropdownItemClick = (language) => {
            state.language = language;
            editor.instance.session.setMode(language);
        }

        return {
            state,
            editor,
            isButtonDisabled,
            getModeId,
            submitCode,
            handleDropdownItemClick,
            isAuthenticated,
        }
    },
};
</script>

<style scoped>
#editor {
    width: 65%;
    height: 88%;
    margin: 0.9%;
    position: absolute;
    top: 9%;
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
    border-radius: 0.5em;
    text-align: center;
    padding: 1%;
}

#submission-details {
    text-align: left;
}
</style>