// Initialize mermaid
mermaid.initialize({
    startOnLoad: true,
    theme: 'default',
    securityLevel: 'loose'
});

// Configure marked options
marked.setOptions({
    breaks: true,
    gfm: true,
    headerIds: true
});

function generateOutline() {
    const inputText = document.getElementById('inputText').value;
    const outputDiv = document.getElementById('outlineOutput');

    if (!inputText.trim()) {
        outputDiv.innerHTML = '<div class="error">Please enter some text first</div>';
        return;
    }

    outputDiv.innerText = 'Generating outline...';

    fetch('/outline', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ outline: inputText })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            outputDiv.innerHTML = `<div class="error">${data.error}</div>`;
        } else {
            outputDiv.setAttribute('data-markdown', data.result);
            outputDiv.innerHTML = marked.parse(data.result);
            mermaid.init(undefined, document.querySelectorAll('.mermaid'));
        }
    })
    .catch(error => {
        console.error('Error:', error);
        outputDiv.innerHTML = `<div class="error">An error occurred while generating the outline</div>`;
    });
}

function switchTab(tab) {
    const diagramView = document.getElementById('diagramView');
    const codeView = document.getElementById('codeView');
    const diagramTab = document.getElementById('diagramTab');
    const codeTab = document.getElementById('codeTab');

    if (tab === 'diagram') {
        diagramView.classList.remove('hidden');
        codeView.classList.add('hidden');
        diagramTab.classList.add('active');
        codeTab.classList.remove('active');
    } else {
        diagramView.classList.add('hidden');
        codeView.classList.remove('hidden');
        diagramTab.classList.remove('active');
        codeTab.classList.add('active');
    }
}

function copyMermaidCode() {
    const code = document.getElementById('mermaidCode').textContent;
    navigator.clipboard.writeText(code).then(() => {
        alert('Mermaid code copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy code:', err);
    });
}

// Additional script functions remain unchanged
