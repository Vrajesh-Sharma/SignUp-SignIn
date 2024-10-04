// background.js

// Basic Three.js setup for background animation
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ alpha: true });

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Particle system setup
const particles = new THREE.BufferGeometry();
const particleCount = 1000;
const positions = [];

for (let i = 0; i < particleCount; i++) {
    const x = (Math.random() - 0.5) * 1000;
    const y = (Math.random() - 0.5) * 1000;
    const z = (Math.random() - 0.5) * 1000;
    positions.push(x, y, z);
}

particles.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

const material = new THREE.PointsMaterial({ color: 0x00ff99, size: 3 });
const particleSystem = new THREE.Points(particles, material);

scene.add(particleSystem);

camera.position.z = 200;

function animate() {
    requestAnimationFrame(animate);

    // Animate the particle system
    particleSystem.rotation.y += 0.001;
    particleSystem.rotation.x += 0.001;

    renderer.render(scene, camera);
}

animate();
