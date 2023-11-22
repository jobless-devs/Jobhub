import express, { Express, Request, Response , Application } from 'express';
import userRouter from './user/routes';

const app: Application = express();
const port = process.env.PORT || 8000;


app.use('/api/v1', userRouter);

app.get('/', (req: Request, res: Response) => {
  res.send('Welcome to JobHub');
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
