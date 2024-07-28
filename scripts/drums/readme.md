# Web Drum Machine with Looper

This project is a web-based drum machine with a built-in looper, created using HTML, CSS, and JavaScript.

## Core Functions Explained

### `createPads()`

This function creates the drum pads based on the `drumSounds` array.

```javascript
function createPads() {
    drumSounds.forEach((drum, index) => {
        const pad = document.createElement('button');
        pad.className = 'drum-pad';
        pad.textContent = drum.name;
        pad.style.backgroundColor = drum.color;
        pad.addEventListener('click', () => playSound(index));
        drumMachine.appendChild(pad);
    });
}
```

For each sound in `drumSounds`:
- Creates a button element
- Sets its class, text, and background color
- Adds a click event listener that plays the corresponding sound
- Appends the button to the drum machine container

### `createSequencer()`

This function creates the sequencer grid.

```javascript
function createSequencer() {
    for (let step = 0; step < 16; step++) {
        for (let sound = 0; sound < drumSounds.length; sound++) {
            const button = document.createElement('button');
            button.className = 'step';
            button.addEventListener('click', () => toggleStep(step, sound));
            sequencer.appendChild(button);
        }
    }
}
```

- Generates a 16x16 grid of buttons (16 steps for each of the 16 sounds)
- Each button is given the 'step' class
- Adds a click event listener to each button that toggles the step on/off

### `toggleStep(step, sound)`

This function is called when a sequencer step is clicked.

```javascript
function toggleStep(step, sound) {
    pattern[step][sound] = !pattern[step][sound];
    updateSequencerUI();
}
```

- Toggles the state of the step in the `pattern` array
- Calls `updateSequencerUI()` to reflect the change visually

### `updateSequencerUI()`

This function updates the visual state of the sequencer.

```javascript
function updateSequencerUI() {
    const steps = sequencer.getElementsByClassName('step');
    for (let i = 0; i < steps.length; i++) {
        const step = Math.floor(i / drumSounds.length);
        const sound = i % drumSounds.length;
        steps[i].classList.toggle('active', pattern[step][sound]);
    }
}
```

- Iterates through all steps in the sequencer
- Toggles the 'active' class based on the state in the `pattern` array

### `playSound(index)`

This function plays a drum sound.

```javascript
function playSound(index) {
    const audio = new Audio(drumSounds[index].sound);
    audio.volume = volumeControl.value;
    audio.play();
}
```

- Creates a new Audio object with the sound URL
- Sets its volume based on the volume control
- Plays the sound

### `playStep()`

This function plays the current step in the sequence.

```javascript
function playStep() {
    pattern[currentStep].forEach((isActive, soundIndex) => {
        if (isActive) playSound(soundIndex);
    });
    
    // Update UI to show current step
    const steps = sequencer.getElementsByClassName('step');
    for (let i = 0; i < drumSounds.length; i++) {
        steps[currentStep * drumSounds.length + i].style.backgroundColor = pattern[currentStep][i] ? '#00ff00' : '#555';
    }
    
    currentStep = (currentStep + 1) % 16;
    
    // Reset previous step color
    // ... (code omitted for brevity)
}
```

- Checks which sounds are active for the current step and plays them
- Updates the visual state of the sequencer to show the current step
- Moves to the next step

### `startLoop()`

This function starts or pauses the loop.

```javascript
function startLoop() {
    if (!isPlaying) {
        isPlaying = true;
        playPauseButton.textContent = 'Pause';
        intervalId = setInterval(playStep, (60 / tempoControl.value) * 1000 / 4);
    } else {
        isPlaying = false;
        playPauseButton.textContent = 'Play';
        clearInterval(intervalId);
    }
}
```

- If not playing, starts the loop and changes button text to 'Pause'
- If already playing, stops the loop and changes button text to 'Play'

### `stopLoop()`

This function stops the loop.

```javascript
function stopLoop() {
    isPlaying = false;
    playPauseButton.textContent = 'Play';
    clearInterval(intervalId);
    currentStep = 0;
    updateSequencerUI();
}
```

- Resets the playing state
- Clears the interval
- Resets the current step to 0
- Updates the sequencer UI

## Event Listeners

```javascript
playPauseButton.addEventListener('click', startLoop);
stopButton.addEventListener('click', stopLoop);
clearButton.addEventListener('click', () => location.reload());

tempoControl.addEventListener('input', () => {
    tempoValue.textContent = `${tempoControl.value} BPM`;
    if (isPlaying) {
        clearInterval(intervalId);
        intervalId = setInterval(playStep, (60 / tempoControl.value) * 1000 / 4);
    }
});

instructionsToggle.addEventListener('click', () => {
    if (instructionsDiv.style.display === 'block') {
        instructionsDiv.style.display = 'none';
        instructionsToggle.textContent = 'Show Instructions';
    } else {
        instructionsDiv.style.display = 'block';
        instructionsToggle.textContent = 'Hide Instructions';
    }
});
```

- Play/Pause button: Starts or pauses the loop
- Stop button: Stops the loop
- Clear button: Refreshes the page, clearing the pattern
- Tempo control: Updates the tempo value display and adjusts the loop interval if playing
- Instructions toggle: Shows or hides the instructions div

This drum machine uses a combination of DOM manipulation, event handling, and timing functions to create an interactive musical instrument in the browser. The core of the functionality lies in the sequencer, which uses a 2D array (`pattern`) to store the state of each step for each sound. The `setInterval` function is used to create the looping behavior, with the interval time calculated based on the current tempo.
