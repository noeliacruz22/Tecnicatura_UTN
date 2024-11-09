<script setup>
import NavBar from './components/NavBar.vue'; 
import DatosPersonales from './components/DatosPersonales.vue'; 
import EducacionComp from './components/EducacionComp.vue';
import ExperienciaComp from './components/ExperienciaComp.vue';
import ProyectosComp from './components/ProyectosComp.vue';
import HabilidadesComp from './components/HabilidadesComp.vue';
import InteresesComp from './components/InteresesComp.vue';
</script>

<template>
  <header id="top">
    <!--barra de navegacion-->
    <NavBar />
    <!--Datos Personales-->
    <DatosPersonales />
    <main>
      <!--El estilo CSS de section se encuentra en base.css-->
        <section id="educacion">
          <h2>Educación - Cursos</h2>
          <!--Componente Educación-->
          <EducacionComp />
        </section>
        <section id="experiencia">
            <h2>Experiencia</h2>
            <!--Componente Experiencia-->
            <ExperienciaComp />
        </section>
        <section id="proyectos">
            <h2>Proyectos</h2>
            <!--Componente Proyectos-->
            <ProyectosComp />
        </section>
        <section id="habilidades">
            <!--Componente Habilidades-->
            <h2>Habilidades</h2>
            <HabilidadesComp />
        </section>
        <section id="intereses">
            <!--Componente Intereses-->
            <h2>Intereses</h2>
            <InteresesComp />
        </section>
    </main>

  </header>
  <footer>
        <a href="#top">Inicio</a>
        <p>© 2024 Noelia Cruz - Portafolio web ♥ - tutorial UTN FRSR</p>
  </footer>

</template>

<style scoped>
footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    font-size: 1.3rem;
}


</style>
