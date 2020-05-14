import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {AppComponent} from './app.component';
import {ProfessorsComponent} from './professors/professors.component';
import {MainComponent} from './main/main.component';
import {ProfessorDetailComponent} from './professor-detail/professor-detail.component';
import {LogInComponent} from './log-in/log-in.component';
import {SignUpComponent} from './sign-up/sign-up.component';
import {LastReviewsResolve} from './last-reviews.resolve';

const routes: Routes = [
  { path: '', component: MainComponent, resolve: { lastReviews: LastReviewsResolve} },
  { path: 'professors', component: ProfessorsComponent },
  { path: 'professors/:id', component: ProfessorDetailComponent },
  { path: 'login', component: LogInComponent },
  { path: 'register', component: SignUpComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
