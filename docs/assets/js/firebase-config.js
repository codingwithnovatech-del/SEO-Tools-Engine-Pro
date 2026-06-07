// === FIREBASE ===
const firebaseConfig = {
  apiKey: "AIzaSyCHsMvmVb7iZNEcJ05bVsqgRCwoITLKkO4",
  authDomain: "seo-tools-engine-pro.firebaseapp.com",
  databaseURL: "https://seo-tools-engine-pro-default-rtdb.firebaseio.com",
  projectId: "seo-tools-engine-pro",
  storageBucket: "seo-tools-engine-pro.firebasestorage.app",
  messagingSenderId: "583592099460",
  appId: "1:583592099460:web:d3e6e157e264e15a738cd1",
  measurementId: "G-JL9JZTFZYH"
};

let db = null;
try {
  if (typeof firebase !== 'undefined') {
    firebase.initializeApp(firebaseConfig);
    db = firebase.database();
  }
} catch (e) {
  console.warn('Firebase init failed:', e.message);
  db = null;
}

// === API KEYS ===
const API_KEYS = {
  pagespeed: "AIzaSyBpwU0KHlP3EQCP31Xlvt03Nywu2MBwCQk",
  deepseek: {
    key: "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",
    host: "api.groq.com"
  },
  openpagerank: "40skw8k84cgowcswwk80ocok80occsk0kw0cw8so"
};
