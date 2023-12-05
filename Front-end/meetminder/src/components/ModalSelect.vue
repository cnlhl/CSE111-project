<template>
    <div v-if="show" class="modal">
      <div class="modal-content">
        <h2>{{ title }}</h2>
        <ul>
          <li v-for="item in items" :key="item" @click="selectItem(item)">{{ item }}</li>
        </ul>
        <button @click="closeModal">关闭</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      show: Boolean,
      items: Array,
      title: String
    },
    emits: ['select', 'close'],
    methods: {
      selectItem(item) {
        this.$emit('select', item);
      },
      closeModal() {
        this.$emit('close');
      }
    }
  };
  </script>
  
  <style scoped>
    .modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .modal-content {
      background-color: white;
      padding: 20px;
      border-radius: 5px;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    li {
      margin-bottom: 10px;
      cursor: pointer;
    }
  </style>
  