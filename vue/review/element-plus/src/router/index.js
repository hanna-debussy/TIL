import { createRouter, createWebHistory } from 'vue-router'
// import VueRouter from 'vue-router'
import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'

import MovieListView from '@/views/MovieListView.vue'

// Vue.use(VueRouter)

const routes = [
  {
    path: '/community',
    name: 'articleList',
    component: ArticleListView,
  },
  {
    path: '/community/:articlePk',
    name: 'articleDetail',
    component: ArticleDetailView,
  },
  {
    path: '/community/new',
    name: 'articleCreate',
    component: ArticleCreateView,
  },
  {
    path: '/community/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView,
  },
  {
    path: '/movies',
    name: 'movieList',
    component: MovieListView,
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
