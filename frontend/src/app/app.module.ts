import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { BannerComponent } from './banner/banner.component';
import { ShortcutComponent } from './shortcut/shortcut.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { UniversitiesComponent } from './universities/universities.component';
import { ReviewAboutUsComponent } from './review-about-us/review-about-us.component';
import { FooterComponent } from './footer/footer.component';
import { PartnersComponent } from './partners/partners.component';
import { MainNewsComponent } from './main-news/main-news.component';
import {LazyLoadScriptService} from './lazy-load-script.service';
import { ProfessorsComponent } from './professors/professors.component';
import { MainComponent } from './main/main.component';
import { SubHeaderComponent } from './sub-header/sub-header.component';
import { ProfessorDetailComponent } from './professor-detail/professor-detail.component';
import {FormsModule} from '@angular/forms';
import { LogInComponent } from './log-in/log-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import {AuthInterceptor} from './auth.interceptor';
import { LastReviewsComponent } from './last-reviews/last-reviews.component';
import { PopupComponent } from './popup/popup.component';
import {LastReviewsResolve} from './last-reviews.resolve';
import { ProfileComponent } from './profile/profile.component';
import { ConfidentialityComponent } from './confidentiality/confidentiality.component';
import {PdfViewerModule} from 'ng2-pdf-viewer';
import {AuthGuard} from './auth.guard';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    BannerComponent,
    ShortcutComponent,
    AboutUsComponent,
    UniversitiesComponent,
    ReviewAboutUsComponent,
    FooterComponent,
    PartnersComponent,
    MainNewsComponent,
    ProfessorsComponent,
    MainComponent,
    SubHeaderComponent,
    ProfessorDetailComponent,
    LogInComponent,
    SignUpComponent,
    LastReviewsComponent,
    PopupComponent,
    ProfileComponent,
    ConfidentialityComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    PdfViewerModule,
  ],
  providers: [LazyLoadScriptService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    },
    LastReviewsResolve,
    AuthGuard,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
