<script setup>
import linkedin from  '/src/assets/linkedin_icon.svg';
import instagram from '/src/assets/instagram_icon.svg';
import github from '/src/assets/github_icon.svg';
import cv from '/src/assets/cv_resume_icon.svg';

const title = 'Noelia Cruz';
const descripcion = 'Técnica Universitaria en Programación - UTN';
const residencia = 'Córdoba, Argentina';
const presentacion = 'Hola, Bienvenidos a mi portafolio de proyectos. Soy una desarrolladora web con experiencia en el desarrollo de aplicaciones web, móviles y de escritorio.';
const redesSociales = [
    { id: 1, name: 'linkedin', src: linkedin, url: 'https://www.linkedin.com/in/noelia-cruz/' },
    { id: 2, name: 'Instagram', src: instagram, url: 'https://www.instagram.com/china.2.2/' },
    { id: 3, name: 'github', src: github, url: 'https://github.com/noeliacruz22' },
    { id: 4, name: 'curriculum', src: cv, url: '' },
];
const telefono = '+54 9 3517633471'; 
</script>

<template>
    <section class="datos-personales">
        <div class="card">
            <h1>{{ title }}</h1>
            <h2>{{ descripcion }}</h2>
            <p>{{ presentacion }}</p>
            <ul class="container-lista">
                <li v-for="red in redesSociales" :key="red.id">
                    <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
                </li>
            </ul>
            <h3>☎ Celular: {{ telefono }}</h3>
            <h4>{{ residencia }}</h4>
        </div>
    </section>
</template>

<style scoped>
h1 {
    font-size: 2.5rem;
}

p {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.card {
    background-color: rgb(28, 41, 52);
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
}

.container-lista {
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

.icon-redsocial {
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover {
    background-color: rgb(28, 41, 52);
    box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
    font-size: 1.2rem;
    font-weight: 600;
}
</style>