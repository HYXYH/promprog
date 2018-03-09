import React from 'react';
import Task from './Task'

const List = ({ items, delCallback }) => (
  <ul>
    <h1>Задачи</h1>
    {
      items && items.map((item) => <Task key={item.id}
                                         id={item.id}
                                         text={item.text}
                                         done={item.done}
                                         delCallback={delCallback}/>)
    }
  </ul>
  );

export default List;
