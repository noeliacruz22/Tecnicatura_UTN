<script setup>
import NavBar from './components/icons/NavBar.vue'; 
import DatosPersonales from './components/icons/DatosPersonales.vue'; 
import EducacionComp from './components/icons/EducacionComp.vue';
import ExperienciaComp from './components/ExperienciaComp.vue';
</script>

<template>
  <header>
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
            <ProyectosComponente />
        </section>
        <section id="habilidades">
            <!--Componente Habilidades-->
            <h2>Habilidades</h2>
            <HabilidadesComponente />
        </section>
        <section id="intereses">
            <!--Componente Intereses-->
            <h2>Intereses</h2>
            <InteresesComponente />
        </section>
    </main>

  </header>


</template>

<style scoped>



</style>
