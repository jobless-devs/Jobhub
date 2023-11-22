import { Request, Response, Router } from 'express';

const userRouter: Router = Router()

userRouter.get('/users', (req: Request, res: Response) => {
  res.send('This is user info');
});

export default userRouter;