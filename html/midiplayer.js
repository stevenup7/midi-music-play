
function begin() {
  // create web audio api context
  const AudioContext = window.AudioContext || window.webkitAudioContext;
  const audioCtx = new AudioContext();

  // create Oscillator and gain node
  const oscillator = audioCtx.createOscillator();
  const gainNode = audioCtx.createGain();
  const delayNode = new DelayNode(audioCtx, {
    delayTime: 0.2,
    maxDelayTime: 2,
  });
  var convolver = audioCtx.createConvolver();
  // connect oscillator to gain node to speakers
  oscillator.connect(gainNode);
  gainNode.connect(convolver);
  convolver.connect(audioCtx.destination);
  //gainNode.connect(audioCtx.destination);

  // set options for the oscillator
  oscillator.detune.value = 20; // value in cents
  oscillator.start(0);
  var isOn = false;

  var counter = 0;
  setGain(audioCtx, gainNode, 0.00001);

  var songInterval = window.setInterval(function () {
    console.log(counter, isOn);
    if(isOn ) {
      setGain(audioCtx, gainNode, 0.01);
    } else {
      if(Math.random() > 0.8){
        setGain(audioCtx, gainNode, 0.2);
      }
    }
    oscillator.frequency.value = 200 + ( Math.random() * 800); // value in cents
    isOn = !isOn;
    if(counter ++ > 50){
      setGain(audioCtx, gainNode, 0.00001);
      window.clearInterval(songInterval);
    }
  }, 100);
}

function noteToFreq(note) {
    let a = 440; //frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12));
}

function setGain(audioCtx, gainNode, val) {
  gainNode.gain.setValueAtTime(gainNode.gain.value, audioCtx.currentTime);
  gainNode.gain.exponentialRampToValueAtTime(val, audioCtx.currentTime + .001);

}
