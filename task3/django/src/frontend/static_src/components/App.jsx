import React, { Component } from 'react';
import './App.css';
import apiUrls from './../constants/apiUrls';
import List from './List';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      term: '',
      items: []
    };
  }

  componentDidMount() {
    fetch(apiUrls.tasks, {
      method: 'GET',
      headers: {
        'content-type': 'application/json'
      },
    })
    .then((res) => res.json())
    .then(data => {
        console.log(data);
      this.setState({
        items: data
      });
    });
  }

  onChange = (event) => {
    this.setState({ term: event.target.value });
  }

  onSubmit = (event) => {
    event.preventDefault();

    fetch(apiUrls.tasks, {
      method: 'POST',
      headers: {
        'content-type': 'application/json'
      },
      body: JSON.stringify({
          text: this.state.term,
          done: false
      })
    })
    .then(res =>
      fetch(apiUrls.tasks)
    )
    .then(res => res.json())
    .then(data => {
      this.setState({
        items: data
      });
    });
  }


  onDelete = (id) => (event) => {
    event.preventDefault();

    fetch(apiUrls.tasks + id + '/', {
      method: 'DELETE',
      headers: {
        'content-type': 'application/json'
      },
    }).then(data => {
        console.log(data);
    })
    .then(res =>
      fetch(apiUrls.tasks)
    )
    .then(res => res.json())
    .then(data => {
      this.setState({
        items: data
      });
    });
  }

  render() {
    return (
      <div>
        <form className="App" onSubmit={this.onSubmit}>
          <input value={this.state.term} onChange={this.onChange} />
          <button>Submit</button>
        </form>
        <List items={this.state.items} delCallback={this.onDelete}/>
      </div>
    );
  }
}
