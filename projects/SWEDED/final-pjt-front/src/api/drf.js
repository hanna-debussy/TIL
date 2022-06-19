const HOST = 'http://localhost:8000/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'community/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'


export default {
  accounts: {
    signup: () => HOST + ACCOUNTS + 'signup/',
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  articles: {
    // /articles/s
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    movieRate: moviePk => HOST + MOVIES + `${moviePk}/` + 'rate/',
    isMovieRated: moviePk => HOST + MOVIES + `${moviePk}/` + 'is_rated/',
    movieRateUpdate: (moviePk, username) => HOST + MOVIES + `${moviePk}/` + 'rate/' + `${username}/`,
    getRecommendation: username => HOST + MOVIES + 'recommendations/' + `${username}/`
  }
}
